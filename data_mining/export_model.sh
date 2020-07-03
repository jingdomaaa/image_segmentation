source activate
conda deactivate
conda activate tensorflow
python ../../../../export_model.py \
    --logtostderr \
    --checkpoint_path="train/model.ckpt-$1" \
    --export_path="export/frozen_inference_graph-$1.pb" \
    --model_variant="xception_65" \
    --atrous_rates=12 \
    --atrous_rates=24 \
    --atrous_rates=36 \
    --output_stride=8 \
    --decoder_output_stride=1 \
    --num_classes=21 \
    --crop_size=513 \
    --crop_size=513 \
    --inference_scales=1.0