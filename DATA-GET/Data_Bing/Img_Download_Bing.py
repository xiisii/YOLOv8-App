from bing_image_downloader import downloader
downloader.download("Cats", limit=100,  output_dir='Data_Bing',adult_filter_off=True, force_replace=False, timeout=60)