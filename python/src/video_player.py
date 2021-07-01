"""A video player class."""
import random
global playing_title
global is_playing


from src.video_library import VideoLibrary
from src.video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.play_status = False
        self.current_video=[]
        self.paused = False
        self.playlist_dict={}
        self.video_list = self._video_library.get_all_videos()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_vids= self._video_library.get_all_videos()
        vids=[]
        sorted_vids=[]
        print("Here's a list of all available videos")
        for vid in all_vids:
            tags="["
            for tag in vid.tags:
                tags += tag + " "
            tags=tags.strip()
            tags += "]"
            vids += [f"{vid.title} ({vid.video_id}) {tags}"]
            sorted_vids = sorted((vids))
        for line in sorted_vids:
            print(line)


    def play_video(self, video_id):
        global playing_title
        global is_playing
        videos = self._video_library.get_all_videos()
        for video in videos:
            if video._video_id == video_id:
                if self.play_status:
                    print("Stopping video:", self.current_video[0])
                print("Playing Video:", video._title)
                self.current_video = [video._title,video._video_id, video._tags]
                self.play_status = True
                self.paused = False
                return
        print("Cannot play video: video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if self.play_status:
            self.play_status = False
            print("Stopping video:", self.current_video[0])
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        global playing_title
        global is_playing
        currently_playing= random.choice(self._video_library.get_all_videos())
        if is_playing == False:
            print(f"Playing video: {currently_playing.title}")
            playing_title = currently_playing.title
            is_playing = True
        elif is_playing == True:
            print(f"Stoppinh video: {playing_title}")
            print(f"Playing video: {currently_playing.title}")
            playing_title = currently_playing.title




        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.play_status:
            print("Pausing video:", self.current_video[0])
            self.paused= True
        else:
            print("Cannot stop video: No video is currently playing")




    def continue_video(self):
        """Resumes playing the current video."""
        if self.play_status:
            if self.paused:
                print("Continuing Video:", self.current_video[0])
                self.paused= False
            else:
                print("Cannot Continue video: video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")



    def show_playing(self):
        """Displays video currently playing."""
        vid_status=""
        if self.play_status:
            if self.paused:
                vid_status= "- PAUSED"

            print("Currently playing:", self.current_video[0]," (",(self.current_video[1]),") ",(self.current_video[2]), vid_status)
        else:
            print(" No video is currently playing")



    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in (name.lower() for name in self.playlist_dict.keys()):
            pl= Playlist(playlist_name)
            self.playlist_dict[playlist_name]=pl
            print("Successfully created a new playlist", pl._name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
