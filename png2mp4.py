import cv2
import os

def create_mp4_from_pngs(src_dir, dst_dir, video_name="output.mp4", fps=30, sort_by="name"):
    """
    Converts PNG files in the src directory to an MP4 video in the dst directory.

    Args:
        src_dir (str): Directory containing PNG files.
        dst_dir (str): Directory to save the MP4 file.
        video_name (str): Name of the output video file. Default is 'output.mp4'.
        fps (int): Frames per second for the video. Default is 30.
        sort_by (str): Sorting method for PNG files. 'name' for alphabetical order, 'time' for modification time. Default is 'name'.
    """
    # Ensure destination directory exists
    os.makedirs(dst_dir, exist_ok=True)

    # Validate video name for special characters
    video_name = video_name.replace(":", "_")

    # Get list of PNG files
    png_files = [f for f in os.listdir(src_dir) if f.endswith(".png")]
    if not png_files:
        print("No PNG files found in the source directory.")
        return

    # Sort PNG files based on the chosen method
    if sort_by == "time":
        png_files.sort(key=lambda f: os.path.getmtime(os.path.join(src_dir, f)))
    else:  # Default to sorting by name
        png_files.sort()

    # Read the first image to get the frame size
    first_image_path = os.path.join(src_dir, png_files[0])
    first_image = cv2.imread(first_image_path)
    if first_image is None:
        print(f"Error: Could not read the first image at {first_image_path}.")
        return
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_path = os.path.join(dst_dir, video_name)
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print(f"Error: VideoWriter could not open {video_path} for writing. Check codec support or file permissions.")
        return

    # Add each PNG file as a frame
    for png_file in png_files:
        image_path = os.path.join(src_dir, png_file)
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Warning: Could not read {image_path}. Skipping.")
            continue
        out.write(frame)

    # Release the video writer and print success message
    out.release()
    if os.path.exists(video_path):
        print(f"Video saved to {video_path}")
    else:
        print(f"Error: Video file was not created at {video_path}.")







src = '/home/hhk-laptop/H-Mobility-Autonomous-Advanced-Course/src/camera_perception_pkg/camera_perception_pkg/lib/Collected_Datasets/2024-12-14-12:48:02'
dst = '/home/hhk-laptop/H-Mobility-Autonomous-Advanced-Course/src/camera_perception_pkg/camera_perception_pkg/lib/Collected_Datasets/2024-12-14-12:48:02'

# Example usage
create_mp4_from_pngs(
    src_dir=src,
    dst_dir=dst,
    video_name="output.mp4",
    fps=24,
    sort_by="time"
)


