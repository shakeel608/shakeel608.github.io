import moviepy.editor as mpe
import os 

path = os.path.join(os.getcwd(), "gallery/NancytoTroyes.mp4")

my_clip = mpe.VideoFileClip(path)
audio_background = mpe.AudioFileClip('quran.mp3')
final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
final_clip = my_clip.set_audio(final_audio)
final_clip.write_videofile("output.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')


