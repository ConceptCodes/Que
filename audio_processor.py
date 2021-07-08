from google.cloud import speech

class Mangekyo():
    def __init__(self, speech):
        self.script = self._transcribe(speech)

    def _transcribe(self, master_audio):
        fragments = []
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=master_audio)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=16000,
            language_code="en-US",
            enable_word_time_offsets=True,
            use_enhanced=True,
            model="video"
        )

        operation = client.long_running_recognize(config=config, audio=audio)

        print("Waiting for operation to complete...")
        result = operation.result(timeout=90)

        for result in result.results:
            alternative = result.alternatives[0]

            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                fragments.append({ word: (start_time, end_time) })
        
        return fragments
        
    def _censor(self, word_list=True, sound=""):
        # if word list, use that
        # if tolerance score, use api to find negative words and then use that as word list, range from 0-0.9
        # will use timestamped hotword detection, and will replace with sound, beep by default
        # i have beeps from 1 - 10s, so words adjacent will have different beep based on length
        pass