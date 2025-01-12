import ffmpeg

def edit_video(voiceover_files, output_file):
    input_clips = [ffmpeg.input(voiceover) for voiceover in voiceover_files]
    ffmpeg.concat(*input_clips, v=1, a=1).output(output_file).run()

if __name__ == "__main__":
    voiceover_files = ["voiceover1.mp3", "voiceover2.mp3"]
    edit_video(voiceover_files, "final_video.mp4")
