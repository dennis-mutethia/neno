-- Table structure for table customers
CREATE TABLE IF NOT EXISTS youtube_videos (
  videoId TEXT PRIMARY KEY,
  title TEXT,
  description TEXT,
  liveBroadcastContent TEXT,
  publishedAt TIMESTAMP
);