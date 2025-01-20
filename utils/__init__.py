from .video_utils import read_video, save_video
from .bbox_utils import get_bbox_width, get_center_of_bbox, measure_distance
def main():
    video_frames = read_video('videos/football.mp4')

    #Save video
    save_video(video_frames, 'output_video/output_video.avi')

if __name__ == '__main__':
    main()