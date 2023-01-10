dbl-extention-img-list.txt

for ext1 in '%20'; do                                                                      
    for ext22 in '.php'; do
        echo "shell$ext1$ext2" >> dbl-extention-img-list.txt
        echo "shell$ext2$ext1" >> dbl-extention-img-list.txt
    done
done

