import discord, os, datetime, time
from discord.ext import commands
from googleapiclient.discovery import build
from dotenv import load_dotenv


class YoutubeAPICog(commands.Cog):
    def __init__(self, yeet_bot):
        self.yeet_bot = yeet_bot
        self.youtube = self.setup_youtube()
    def setup_youtube(self):
        return build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))
    @commands.command(name="dsn")
    async def role_set_choose(self, context: commands.Context, *args):

        request = self.youtube.channels().list(
            part="contentDetails",
            id="UC9OmOMZS6rU0_jIdZOxSHxw"
        )
        response = request.execute()
        uploads_playlist = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        request = self.youtube.playlistItems().list(
            part="snippet",
            maxResults=1,
            playlistId=uploads_playlist
        )
        response = request.execute()

        recent_video = response["items"][0]["snippet"]

        #date stuff
        date_time = datetime.datetime.strptime(recent_video["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
        unix_epoch = time.mktime(date_time.timetuple())
        upload_date = f"<t:{str(unix_epoch)[:-2]}>"

        recent_video_title = recent_video["title"]
        recent_video_thumbnail = recent_video["thumbnails"]["maxres"]["url"]

        await context.send(recent_video_title + " | Uploaded: " + upload_date)
        await context.send(recent_video_thumbnail)

async def setup(yeet_bot):
    await yeet_bot.add_cog(YoutubeAPICog(yeet_bot))
