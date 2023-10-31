from bottle import route, run, request, template
from yt_dlp import YoutubeDL
from datetime import datetime


# Bottle route to handle the form input and display results
@route("/", method="GET")
def video_analysis():
    # Check if the form has been submitted
    if request.GET.get("submit"):
        video_url = request.GET.get("video_url")

        try:
            # Function to fetch video details using yt-dlp
            def get_video_details(video_url):
                ydl_opts = {}
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(video_url, download=False)

                    # Explicitly convert the numeric values to integers
                    views = int(info.get("view_count", 0))
                    likes = int(info.get("like_count", 0))
                    dislikes = int(0.2 * (views - likes))
                    title = info.get("title", "N/A")
                    author = info.get("uploader", "N/A")
                    description = info.get("description", "N/A")
                    keywords = info.get("keywords", "N/A")
                    publish_date = datetime.strptime(
                        info.get("upload_date", "N/A"), "%Y%m%d"
                    )
                    length = int(info.get("duration", 0))
                    thumbnail_url = info.get("thumbnail", "N/A")

                    # Calculate like-to-dislike ratio
                    like_dislike_ratio = (likes / (likes + dislikes)) * 100

                    # Calculate engagement rate
                    engagement_rate = ((likes + dislikes) / views) * 100

                    # Calculate days since publish
                    days_since_publish = (datetime.now() - publish_date).days

                    # Determine rating category
                    if likes >= dislikes * 10:
                        rating_category = "Excellent"
                    elif likes >= dislikes * 5:
                        rating_category = "Good"
                    elif likes >= dislikes:
                        rating_category = "Fair"
                    else:
                        rating_category = "Poor"

                    return template(
                        "video_details",
                        title=title,
                        author=author,
                        description=description,
                        views=views,
                        likes=likes,
                        dislikes=dislikes,
                        publish_date=publish_date,
                        keywords=keywords,
                        length=length,
                        thumbnail_url=thumbnail_url,
                        like_dislike_ratio=like_dislike_ratio,
                        engagement_rate=engagement_rate,
                        days_since_publish=days_since_publish,
                        rating_category=rating_category,
                    )

                return "Error: Video details not found."

            return get_video_details(video_url)

        except Exception as e:
            error_message = f"Error: {str(e)}"
            return template("error", error_message=error_message)

    # If the form hasn't been submitted, render the input form
    return template("video_form")


if __name__ == "__main__":
    run(host="localhost", port=8080)
