import pytube
#url='https://www.youtube.com/watch?v=GN-kb2lHspM'
url2 ='https://youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0'
#yt = pytube.YouTube(url)
yt2 = pytube.Playlist(url2)
#stream=yt2.streams
#print(stream)
#video = stream.filter(res='720p').desc().first()
 
#video.download(r'Z:\уроки с ютуба питон')
for video in yt2.videos:
  video.streams.filter(res='720p').first().download(r'')
  