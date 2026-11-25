from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.varLib.instancer import instantiateVariableFont
import math, cairosvg
F='/home/claude/brand/fonts/'
cin=instantiateVariableFont(TTFont(F+'Cinzel[wght].ttf'),{'wght':700})
nun=instantiateVariableFont(TTFont(F+'Nunito[wght].ttf'),{'wght':700})
def run(font,text,size,x,y,track=0):
    gs=font.getGlyphSet(); cmap=font.getBestCmap(); s=size/font['head'].unitsPerEm; d=''; cx=x
    for ch in text:
        g=cmap.get(ord(ch)); 
        if g is None: cx+=size*0.3; continue
        pen=SVGPathPen(gs); gs[g].draw(TransformPen(pen,(s,0,0,-s,cx,y))); d+=pen.getCommands(); cx+=gs[g].width*s+track
    return d,cx
def width(font,text,size,track=0):
    return run(font,text,size,0,0,track)[1]
def star(cx,cy,r1,r2):
    pts=[]
    for i in range(16):
        r=r1 if i%2==0 else r2; a=math.pi/8*i-math.pi/2
        pts.append(f'{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}')
    return 'M'+' L'.join(pts)+'Z'
def emblem(cx,cy,s,col,line='#1F4D3A',fill='none'):
    def oct8(r):
        import math
        pts=[]
        for i in range(16):
            rr=r if i%2==0 else r*0.74; a=math.pi/8*i-math.pi/2
            pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
        return 'M'+' L'.join(pts)+'Z'
    k=s
    return (f'<path d="{oct8(36*k)}" fill="{fill}" stroke="{line}" stroke-width="{3.2*k}" stroke-linejoin="round"/>'
            f'<path d="{oct8(29*k)}" fill="none" stroke="{col}" stroke-width="{1.6*k}" stroke-linejoin="round"/>'
            f'<path d="M{cx} {cy-6*k} C{cx-6*k} {cy-18*k} {cx-17*k} {cy-14*k} {cx-12*k} {cy-6*k} C{cx-9*k} {cy-3*k} {cx-4*k} {cy-4*k} {cx} {cy-6*k}Z" fill="none" stroke="{col}" stroke-width="{2.6*k}" stroke-linejoin="round"/>'
            f'<path d="M{cx} {cy-6*k} C{cx+6*k} {cy-18*k} {cx+17*k} {cy-14*k} {cx+12*k} {cy-6*k} C{cx+9*k} {cy-3*k} {cx+4*k} {cy-4*k} {cx} {cy-6*k}Z" fill="none" stroke="{col}" stroke-width="{2.6*k}" stroke-linejoin="round"/>'
            f'<path d="M{cx-17*k} {cy-3*k} H{cx+17*k}" stroke="{line}" stroke-width="{3*k}" stroke-linecap="round"/>'
            f'<path d="M{cx} {cy-5*k} V{cy+16*k}" stroke="{line}" stroke-width="{3*k}" stroke-linecap="round"/>'
            f'<path d="M{cx} {cy-3*k} L{cx-7*k} {cy+8*k} M{cx} {cy-3*k} L{cx+7*k} {cy+8*k}" stroke="{col}" stroke-width="{2*k}" stroke-linecap="round"/>')

def logo(name, main, gold, sub, bg=None):
    W=560; H=150
    w1=width(cin,'SAFAR GIFTS',52,2)
    x0=110
    d1,_=run(cin,'SAFAR GIFTS',52,x0,78,2)
    d2,_=run(nun,'BY KURNIA TOUR & TRAVEL',15,x0+2,112,3.2)
    W=int(max(x0+w1, x0+width(nun,'BY KURNIA TOUR & TRAVEL',15,3.2))+24)
    b=f'<rect width="{W}" height="{H}" rx="20" fill="{bg}"/>' if bg else ''
    sv=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Safar Gifts by Kurnia Tour and Travel">{b}'
        f'{emblem(52,72,1.15,gold, main if bg is None else gold, "#FBF6EC" if bg is None else "none")}<path fill="{main}" d="{d1}"/><line x1="{x0}" y1="92" x2="{x0+w1}" y2="92" stroke="{gold}" stroke-width="1.5"/><path fill="{sub}" d="{d2}"/></svg>')
    open(f'build/assets/{name}.svg','w').write(sv)
    cairosvg.svg2png(bytestring=sv.encode(),write_to=f'/tmp/{name}.png',output_width=560)
logo('safar-logo','#1F4D3A','#B08D3E','#6B1E2A')
logo('safar-logo-reverse','#FBF6EC','#D4B56A','#E9DCC4','#1F4D3A')
# icon
sv=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><rect width="128" height="128" rx="28" fill="#1F4D3A"/>{emblem(64,64,1.45,"#D4B56A","#D4B56A")}</svg>'
open('build/assets/safar-icon.svg','w').write(sv)
