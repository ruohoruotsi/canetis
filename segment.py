class Segment(object):
    """
    Class to store start/end values
    of an audio file relative to the overall file
    during a recursive call
    """

    def __init__(self, start_audio, end_audio, gentle_output, aligned, audio_file, parent_seg_len):
        """
        Initialize start audio to be the start of the segment
        being recursively called, then update that value
        """
        self.start_audio = start_audio
        self.end_audio = end_audio
        self.gentle = gentle_output
        self.aligned = aligned
        self.audio_file = audio_file
        self.parent_seg_len = parent_seg_len


    def get_text(self):
        """
        get the text to pass
        into gentle from the dictionary
        values of gentle
        """
        words = [word.word for word in self.gentle]
        text = " ".join(words)
        return text

    def get_anchor_length(self):

        """
        Helper Function that automatically choose canetis'
        anchor length based on the gentle output error rate.
        The greater the error rate, the greater the anchor length

        Outputs
        -------------------
        An int that should be used to select the anchor length
        """

        # prevent disporportionate anchor_lengths
        anchor_length = int(max(len(self.gentle)//8, 4))

        return anchor_length
