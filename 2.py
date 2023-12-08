# write a code for converting video to audio and store in a folder
import moviepy.editor as mp
clip = mp.VideoFileClip("video.mp4")
clip.audio.write_audiofile("audio.mp3")