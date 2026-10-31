# Day 3: Testing Real Rasterio and GDAL Linkage

import rasterio
from rasterio.io import MemoryFile
import numpy as np

def create_and_inspect_dummy_geotiff():
    print("=== Testing Real Rasterio & GDAL C-Binaries ===")
    
    # Create a small dummy raster array in memory (1 band, 100x100 pixels)
    array = np.ones((1, 100, 100), dtype=np.uint8)
    
    # Define basic spatial metadata (Affine transform and CRS)
    from rasterio.transform import from_origin
    transform = from_origin(320000.0, 5810240.0, 1.0, 1.0) # xmin, ymin, xsize, ysize
    
    # Write a temporary GeoTIFF into memory using Rasterio
    with MemoryFile() as memfile:
        with memfile.open(
            driver='GTiff',
            height=100,
            width=100,
            count=1,
            dtype=array.dtype,
            crs='EPSG:7855',
            transform=transform
        ) as dataset:
            dataset.write(array)
            
        # Re-open from memory to read it back like a real file
        with memfile.open() as dataset:
            print(f"Successfully created & read GeoTIFF!")
            print(f"CRS Found        : {dataset.crs}")
            print(f"Dataset Shape    : {dataset.shape}")
            print(f"Affine Transform : \n{dataset.transform}")

if __name__ == "__main__":
    create_and_inspect_dummy_geotiff()
    print("\nDay 3 Real Rasterio status: SUCCESS!")