import drawSvg as draw
import uuid

#base is needed, and clipart/ title are the different ones
#can be a dict theme to distinguish them

themes = {
    'poptag': ['264653','2A9D8F','E9C46A','F4A261','E76F51'] ,
    'speed': ['E63946','F1FAEE','A8DADC','457B9D','1D3557'] ,
    'overlay': ['FF99C8','FCF6BD','D0F4DE','A9DEF9','E4C1F9']
}

class QueCard():
    def __init__(self,type,duration,meta):
        self.type = type
        self.meta = meta
        self.duration = duration
        self.base = draw.Drawing(1080, 1080, origin='center', displayInline=False)
        self.current_theme = themes[self.type]

    def _draw_base(self):
        # basically a square with a rounded base
        base = draw.Rectangle(33, 289, 921, 712, fill='#E4E6F2')
        base.append(draw.Line(99, 925, 798, 0), stroke="black")
        base.append(draw.Text('Perspectives v1.0', 30, 353, 943, fill="grey"))
        return base

    def _draw_top_clip(self):
        pass

    def _draw_clip(self):
        # a square with slanted rectangle accents
        clip = draw.Rectangle(15, 260, 958, 92, fill="#302E39")
        start_x = 275
        for color,index in enumeration(current_theme['col']):
            clip.append(draw.Rect(start_x+(index*169), 259, 169, 92), fill=color)
        return clip

    def _draw_bracket(self):
        pass

    def _text_needed(self):
        tmp = {
            'title': '</{}>'.format(str(self.type).capitalize()),
            'scene': 'que-{}'.format(str(uuid.uuid1())),
            'duration': self.duration,
            'meta': self.meta
        }

    def _render(self):
        pass