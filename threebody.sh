while getopts f:g: arg 
do
    case $arg in
        f) FILE=$OPTARG 
            ;;
        g) GPU=$OPTARG

    esac
done

  python generate.py -p "a painting of three suns orbs rotating in sky | dystopian | physics alpha centauri | trending artstation" \
                      --output ./3BP/3bp$FILE.png \
                      -conf "checkpoints/wikiart_16384.yaml" \
                      -ckpt "checkpoints/wikiart_16384.ckpt" \
                      -cd cuda:$GPU
