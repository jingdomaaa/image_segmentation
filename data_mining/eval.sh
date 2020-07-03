source activate
conda deactivate
conda activate tensorflow
python ../../../../eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=12 \
    --atrous_rates=24 \
    --atrous_rates=36 \
    --output_stride=8 \
    --decoder_output_stride=1 \
    --eval_crop_size=513,513 \
    --checkpoint_dir="train/" \
    --eval_logdir="eval/" \
    --dataset_dir="../../tfrecord/" &
    # --max_number_of_evaluations=1 &