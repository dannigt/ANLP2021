wget -nc https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip
unzip -o wiki-news-300d-1M.vec.zip 

head -10000 wiki-news-300d-1M.vec > ./small.vec
