@echo
echo _
echo =====================
echo CONSIDER RENAMING!!!
echo =====================
echo _
IF NOT EXIST ".\documents" (
   MKDIR "documents"
)
IF NOT EXIST ".\presentations" (
   MKDIR "presentations"
)
IF NOT EXIST ".\videos" (
   MKDIR "videos"
)
IF NOT EXIST ".\images" (
   MKDIR "images"
)
IF NOT EXIST ".\sounds" (
   MKDIR "sounds"
)
IF NOT EXIST ".\programs" (
   MKDIR "programs"
)
IF NOT EXIST ".\zip" (
   MKDIR "zip"
)
IF NOT EXIST ".\tables" (
   MKDIR "tables"
)


move /-Y *.txt documents
move /-Y *.doc* documents
move /-Y *.pdf documents
move /-Y *.pptx presentations 
move /-Y *.mp4 videos
move /-Y *.jpg images
move /-Y *.jpeg images
move /-Y *.png images
move /-Y *.gif images
move /-Y *.webp images
move /-Y *.mp3 sounds
move /-Y *.exe programs
move /-Y *.zip zip
move /-Y *.7z zip
move /-Y *.xlsx tables
move /-Y *.csv tables
move /-Y *.py programs

