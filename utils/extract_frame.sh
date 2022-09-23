# Pull frame out of a video.  Maybe useful for thumbnail.
# pass mp3 file location as first arg,
# pass frame number as second arg
movie=$1
framenum=$2

sel=between\(n,${framenum},${framenum}\)
#echo $sel

ffmpeg -i $movie -vf select=\'$sel\' -vsync 0 -start_number $framenum frame%d.png
