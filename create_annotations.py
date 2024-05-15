from pathlib import Path
'''
image_e = {"id":4,
 "width":1046,
 "height":940,
 "file_name":"_data3_qilei_chen_DATA_息肉分类标注2023_4_7_20230815_传统型锯齿状息肉_17325641_201703_images_polyp-classification_juchizhuangxirou_chuantong_2017_20170329101500_17325651_01.201503110051_images_img-00058-00001.jpg",
 "license":0,
 "flickr_url":"",
 "coco_url":"",
 "date_captured":0}
'''
def create_image_annotation(file_path: Path, width: int, height: int, image_id: int):
    file_path = file_path.name
    image_annotation = {
        "file_name": file_path,
        "height": height,
        "width": width,
        "id": image_id,
        "license":0,
        "flickr_url":"",
        "coco_url":"",
        "date_captured":0
    }
    return image_annotation
'''
ann_e = {"id":1,
         "image_id":1,
         "category_id":1,
         "segmentation":[],
         "area":99723.0264,
         "bbox":[283.44,267.61,294.96,338.09],
         "iscrowd":0,
         "attributes":{"occluded":false,"rotation":0.0}}
'''
def create_annotation_from_yolo_format(
    min_x, min_y, width, height, image_id, category_id, annotation_id, segmentation=True
):
    bbox = (float(min_x), float(min_y), float(width), float(height))
    area = width * height
    max_x = min_x + width
    max_y = min_y + height
    if segmentation:
        seg = [[min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y]]
    else:
        seg = []

    annotation = {
        "id": annotation_id,
        "image_id": image_id,
        "bbox": bbox,
        "area": area,
        "iscrowd": 0,
        "category_id": category_id,
        "segmentation": seg,
        "attributes": {"occluded":0,"rotation":0.0}
    }

    return annotation

def create_annotation_from_yolo_results_format(
    min_x, min_y, width, height, image_id, category_id, conf
):
    bbox = (float(min_x), float(min_y), float(width), float(height))
    
    annotation = [{
        "image_id": image_id,
        "category_id": category_id,
        "bbox": bbox,
        "score": conf
    }]

    return annotation

# Create the annotations of the ECP dataset (Coco format)
coco_format = {"images": [{}], "categories": [], "annotations": [{}]}
