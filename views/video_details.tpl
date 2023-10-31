<!DOCTYPE html>
<html>
<head>
    <title>Video Details</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/vidito/vidicss@1.2/styles.min.css">
</head>
<body>
    <h1>Video Details</h1>
    <h2>Title: {{ title }}</h2>
    <p>Author: {{ author }}</p>
    <p>Description: {{ description }}</p>
    <p>Views: {{ views }}</p>
    <p>Likes: {{ likes }}</p>
    <p>Dislikes: {{ dislikes }}</p>
    <p>Publish Date: {{ publish_date }}</p>
    <p>Keywords: {{ keywords }}</p>
    <p>Length (seconds): {{ length }}</p>
    <img src="{{ thumbnail_url }}" alt="Video Thumbnail">
    <p>Like-to-Dislike Ratio: {{ like_dislike_ratio }}%</p>
    <p>Engagement Rate: {{ engagement_rate }}%</p>
    <p>Days Since Publish: {{ days_since_publish }} days</p>
    <p>Rating Category: {{ rating_category }}</p>
</body>
</html>
