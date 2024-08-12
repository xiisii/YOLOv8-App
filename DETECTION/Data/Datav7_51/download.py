import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.utils.random as four

    # The path to export the dataset
EXPORT_DIR = "C:/Users/hvthy/Desktop/DoAn2/SEGMENTATION/Data/Data_v7/Dataset"

    # Prepare train split

train = foz.load_zoo_dataset(
    "open-images-v7",
    split="train",
    label_types=["segmentations"],
    classes=["Dog"],
    max_samples=100,
)

    # YOLO format requires a common classes list
classes = train.default_classes

train.export(
    export_dir=EXPORT_DIR,
    dataset_type=fo.types.YOLOv5Dataset,
    split="train",
    classes=classes,
)

    # Prepare validation split

validation = foz.load_zoo_dataset(
    "open-images-v7",
    split="validation",
    label_types=["segmentations"],
    classes=["Dog"],
    max_samples=100,
)

validation.export(
    export_dir=EXPORT_DIR,
    dataset_type=fo.types.YOLOv5Dataset,
    split="val",  # Ultralytics uses 'val'
    classes=classes,
)