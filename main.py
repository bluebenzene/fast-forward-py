from moviepy.editor import VideoFileClip, vfx

def fast_forward_video(input_file, output_file, speed_factor=16):
    """
    Speeds up the input video by the specified speed factor.

    Parameters:
    - input_file: Name of the input video file (e.g., 'recording.mp4').
    - output_file: Name of the output video file (e.g., 'fast_forwarded.mp4').
    - speed_factor: Factor by which the video will be sped up (e.g., 16).
    """
    # Load the video
    clip = VideoFileClip(input_file)

    # Speed up the video
    fast_clip = clip.fx(vfx.speedx, speed_factor)

    # Write the fast-forwarded video to a file
    fast_clip.write_videofile(output_file, codec='libx264')
    print(f'Fast-forwarded video saved to {output_file}')

# Example usage
if __name__ == "__main__":
    # Provide the path to your recorded video from ShareX
    input_video_path = "recording.mp4"  # Change this to the path of your video file
    output_video_path = "fast_forwarded.mp4"

    # Fast forward the video by 16x
    fast_forward_video(input_video_path, output_video_path, speed_factor=16)
