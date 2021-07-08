"""
    This is where we process and render the video
"""

import moviepy.editor as mp

class Chidori(self):
    def __init__(self, input_path, output_path="test/output.mp4"):
        self.input_path= input_path 
        self.output_path= output_path
        self.video= self._load()

    def _load(self):
        return mp.VideoFileClip(self.input_path)

    def _get_frames(self):
        return self.video

    def _get_audio(self):
        path = self.output_path+'/dialogue.wav'
        mp.audio.write_audiofile(path)
        print('Audio file saved to {}'.format(path))

    def _preview(self):
        # show a gui window of the current video
        pass

    def _render(self):      
        my_clip.write_videofile(self.output_path)
        print('Movie saved to {}'.format(self.output_path))