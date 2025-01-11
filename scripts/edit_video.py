from moviepy.editor import VideoFileClip, concatenate_videoclips

def edit_video(clips, output_path):
    video_clips = [VideoFileClip(clip) for clip in clips]
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(output_path)

if __name__ == "__main__":
    clips = ["clip1.mp4", "clip2.mp4"]
    output_path = "static/thumbnails/final_video.mp4"
    edit_video(clips, output_path)
