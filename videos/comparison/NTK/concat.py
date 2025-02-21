# from moviepy import VideoFileClip, clips_array

# # 读取视频文件
# video1 = VideoFileClip("Yarn.mp4")
# video2 = VideoFileClip("Yarn2.mp4")



# # 竖向拼接
# final_video = clips_array([[video1], [video2]])

# # 输出最终视频
# final_video.write_videofile("Yarnnew.mp4")
from moviepy import VideoFileClip, clips_array

# 读取视频文件
video1 = VideoFileClip("ours1.mp4")
video2 = VideoFileClip("ours2.mp4")
video3 = VideoFileClip("ours3.mp4")

# 横向拼接
final_video = clips_array([[video1, video2, video3]])

# 输出最终视频
final_video.write_videofile("ours.mp4")
