from PIL import Image, ImageDraw, ImageFont
import math, os, subprocess, tempfile, argparse
import numpy as np

W,H,FPS,DURATION = 1920,1080,24,15
FRAMES = FPS*DURATION
parser = argparse.ArgumentParser()
parser.add_argument('--output', default='/tmp/lymi-product-film.mp4')
OUT = parser.parse_args().output
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts = {
 'title': ImageFont.truetype(FONT_BOLD, 58),
 'body': ImageFont.truetype(FONT_REG, 30),
 'small': ImageFont.truetype(FONT_MONO, 21),
 'micro': ImageFont.truetype(FONT_MONO, 17),
 'logo': ImageFont.truetype(FONT_BOLD, 148),
 'node': ImageFont.truetype(FONT_BOLD, 25),
}
WHITE=(248,248,248); MUTED=(157,160,165); SILVER=(205,208,214)

def clamp(x,a=0,b=1): return max(a,min(b,x))
def ease(x):
    x=clamp(x); return x*x*(3-2*x)
def smoothstep(a,b,x): return ease((x-a)/(b-a))
def rounded(d,box,r,fill,outline=None,width=2):
    d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)
def text_fade(d,xy,txt,font,fill,alpha,anchor='mm'):
    d.text(xy,txt,font=font,fill=(*fill,int(255*clamp(alpha))),anchor=anchor)
def line_glow(im,points,fill=(240,240,245),width=5):
    ImageDraw.Draw(im).line(points,fill=(*fill,225),width=width,joint='curve')

def make_background():
    yy,xx=np.mgrid[0:H:4,0:W:4]
    dist=np.sqrt(((xx-W*.5)/(W*.72))**2+((yy-H*.47)/(H*.85))**2)
    v=(9*np.maximum(0,1-dist)**2).astype(np.uint8)
    arr=np.zeros((H//4,W//4,3),dtype=np.uint8)
    arr[:,:,0]=5+v; arr[:,:,1]=5+v; arr[:,:,2]=7+v
    base=Image.fromarray(arr,'RGB').resize((W,H),Image.Resampling.BILINEAR).convert('RGBA')
    d=ImageDraw.Draw(base)
    for x in range(80,W,120): d.line((x,0,x,H),fill=(19,20,23,85),width=1)
    for y in range(60,H,120): d.line((0,y,W,y),fill=(19,20,23,85),width=1)
    d.line((110,H-92,W-110,H-92),fill=(42,44,49,170),width=1)
    return base
BACKGROUND=make_background()

def draw_phone(im,cx,cy,s,p):
    d=ImageDraw.Draw(im); w=int(112*s); h=int(180*s)
    rounded(d,(cx-w//2,cy-h//2,cx+w//2,cy+h//2),22*s,(12,13,15,255),outline=(238,240,244,230),width=max(2,int(5*s)))
    d.rounded_rectangle((cx-22*s,cy-h//2+15*s,cx+22*s,cy-h//2+21*s),radius=3,fill=WHITE)
    d.ellipse((cx-7*s,cy+h//2-19*s,cx+7*s,cy+h//2-5*s),outline=WHITE,width=2)
    for i in range(3):
        r=(100+i*48)*s
        d.arc((cx-r,cy-r,cx+r,cy+r),start=215,end=325,fill=(245,246,248,int(220*(1-i*.2))),width=4)

def scene_phone(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.22,p)*(1-smoothstep(.88,1,p))
    cx=int(960+130*math.sin(p*math.pi)); cy=450
    draw_phone(im,cx,cy,1.12,p)
    for i in range(5):
        q=(p*1.6-i*.16)%1; r=170+q*210
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(240,242,245,int(110*(1-q)*a)),width=3)
    title_a=smoothstep(.18,.38,p)*(1-smoothstep(.9,1,p))
    text_fade(d,(150,140),'01  /  CAPTURE',fonts['micro'],MUTED,a,'lm')
    text_fade(d,(960,790),'EVERY CALL IS A CHANCE',fonts['small'],SILVER,title_a)
    text_fade(d,(960,865),'Never miss the next conversation.',fonts['title'],WHITE,title_a)

def scene_reply(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.18,p)*(1-smoothstep(.9,1,p))
    text_fade(d,(150,140),'02  /  RESPOND',fonts['micro'],MUTED,a,'lm')
    x1=int(-450+760*ease(p)); x2=int(2370-760*ease(max(0,p-.22)/.78))
    rounded(d,(x1,290,x1+520,390),22,(18,19,22,int(255*a)),outline=(230,232,236,int(255*a)),width=2)
    d.text((x1+25,340),'Thanks for calling. How can we help?',font=fonts['body'],fill=(245,246,248,int(255*a)),anchor='lm')
    rounded(d,(x2-560,430,x2,530),22,(18,19,22,int(235*a)),outline=(230,232,236,int(235*a)),width=2)
    d.text((x2-25,480),'I need to book a service.',font=fonts['body'],fill=(245,246,248,int(235*a)),anchor='rm')
    q=smoothstep(.48,.78,p); by=int(700+90*(1-q))
    rounded(d,(700,by-65,1220,by+65),24,(15,16,18,int(245*q)),outline=(230,232,236,int(190*q)),width=2)
    d.ellipse((750,by-18,786,by+18),outline=(245,245,248,int(255*q)),width=3)
    text_fade(d,(815,by),'Appointment request captured',fonts['body'],WHITE,q,'lm')
    text_fade(d,(960,865),'Reply. Qualify. Book or hand off.',fonts['title'],WHITE,a)

def scene_inbox(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.18,p)*(1-smoothstep(.9,1,p))
    text_fade(d,(150,140),'03  /  UNIFY',fonts['micro'],MUTED,a,'lm')
    cx,cy=960,475
    channels=[('CALL',-math.pi/2),('CHAT',0),('MAIL',math.pi/2),('SOCIAL',math.pi)]
    for idx,(lab,ang) in enumerate(channels):
        rad=370; tx=cx+int(rad*math.cos(ang)); ty=cy+int(rad*.62*math.sin(ang))
        q=smoothstep(.1+idx*.08,.45+idx*.08,p)
        rounded(d,(tx-105,ty-42,tx+105,ty+42),22,(18,19,22,int(240*q)),outline=(218,221,226,int(220*q)),width=2)
        text_fade(d,(tx,ty),lab,fonts['small'],WHITE,q)
        end=(cx+(tx-cx)*.58,cy+(ty-cy)*.58)
        line_glow(im,[(tx,ty),end],(210,214,220),3)
    q=smoothstep(.42,.78,p)
    rounded(d,(cx-175,cy-110,cx+175,cy+110),34,(10,11,13,int(255*q)),outline=(250,250,252,int(240*q)),width=3)
    text_fade(d,(cx,cy-12),'LYMI',fonts['title'],WHITE,q)
    text_fade(d,(cx,cy+54),'INBOX',fonts['micro'],MUTED,q)
    text_fade(d,(960,865),'One inbox. Clear human hand-off.',fonts['title'],WHITE,a)

def scene_studio(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.15,p)*(1-smoothstep(.9,1,p))
    text_fade(d,(150,140),'04  /  BUILD',fonts['micro'],MUTED,a,'lm')
    labels=['TRIGGER','AI STEP','OUTPUT']; xs=[470,960,1450]; y=470
    prog=smoothstep(.05,.75,p)
    for i in range(2):
        endx=xs[i]+(xs[i+1]-xs[i])*prog
        line_glow(im,[(xs[i]+125,y),(endx-125,y)],(226,229,234),5)
    for i,(x,lab) in enumerate(zip(xs,labels)):
        q=smoothstep(.12+i*.15,.45+i*.15,p); size=1+0.025*math.sin(p*math.pi*2+i)
        ww=int(250*size); hh=int(170*size)
        rounded(d,(x-ww//2,y-hh//2,x+ww//2,y+hh//2),26,(17,18,20,int(250*q)),outline=(240,242,246,int(230*q)),width=3)
        d.ellipse((x-12,y-12,x+12,y+12),fill=(250,250,252,int(255*q)))
        text_fade(d,(x,y+55),lab,fonts['node'],WHITE,q)
    text_fade(d,(960,760),'Create. Test. Debug. Deploy.',fonts['title'],WHITE,a)
    text_fade(d,(960,845),'From a sentence to a working workflow.',fonts['body'],MUTED,a)

def scene_market(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.18,p)*(1-smoothstep(.9,1,p))
    text_fade(d,(150,140),'05  /  MARKETPLACE',fonts['micro'],MUTED,a,'lm')
    for i in range(12):
        row,col=divmod(i,4); x=520+col*295; y=300+row*155
        q=smoothstep(i*.035,i*.035+.38,p); w=220; h=108
        rounded(d,(x-w//2,y-h//2,x+w//2,y+h//2),18,(18,19,22,int(235*q)),outline=(190,194,201,int(210*q)),width=2)
        for k in range(3):
            rr=6; d.ellipse((x-34+k*20-rr,y-12-rr,x-34+k*20+rr,y-12+rr),fill=(245,246,248,int(240*q)))
        text_fade(d,(x,y+25),['AGENTS','APPS','AUTOMATION','SERVICES'][col],fonts['micro'],SILVER,q)
    text_fade(d,(960,840),'Discover. Test. Buy. Build. Sell.',fonts['title'],WHITE,a)

def scene_end(im,p):
    d=ImageDraw.Draw(im); a=smoothstep(0,.24,p); cx,cy=960,440
    for i in range(4):
        r=170+i*58+int(16*math.sin(p*math.pi*2+i))
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(190,194,202,int(45*a)),width=2)
    text_fade(d,(960,440),'LYMI',fonts['logo'],WHITE,a)
    text_fade(d,(960,590),'AI AGENTS  ·  AUTOMATION  ·  MARKETPLACE',fonts['small'],SILVER,a)
    text_fade(d,(960,700),'by NOBLESS',fonts['body'],MUTED,a)
    text_fade(d,(960,930),'BUILDING INTELLIGENCE. CREATING POSSIBILITIES.',fonts['micro'],MUTED,a)

def render_frame(i):
    t=i/FPS; im=BACKGROUND.copy(); scene=int(t//3); p=(t-scene*3)/3
    if scene==0: scene_phone(im,p)
    elif scene==1: scene_reply(im,p)
    elif scene==2: scene_inbox(im,p)
    elif scene==3: scene_studio(im,p)
    elif scene==4: scene_market(im,p)
    else: scene_end(im,p)
    grain=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(grain)
    for k in range(240):
        gd.point(((k*7919+i*37)%W,(k*104729+i*53)%H),fill=(220,224,230,9))
    im.alpha_composite(grain)
    return im.convert('RGB')

with tempfile.TemporaryDirectory(prefix='lymi_frames_') as td:
    for i in range(FRAMES):
        render_frame(i).save(os.path.join(td,f'{i:05d}.png'),compress_level=1)
    cmd=['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',os.path.join(td,'%05d.png'),'-c:v','libx264','-preset','slow','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart',OUT]
    subprocess.run(cmd,check=True)
print(OUT)