# Day 3: Inspecting Geospatial Metadata with Rasterio Concepts

class MockRasterDataset:
    """Simulates how Rasterio reads GeoTIFF metadata attributes"""
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.count = 4  # Number of bands (e.g., Red, Green, Blue, NIR)
        self.crs = "EPSG:7855"  # GDA2020 / Vicgrid projection
        self.bounds = (320000.0, 5800000.0, 330240.0, 5810240.0) # (xmin, ymin, xmax, ymax)

def inspect_raster():
    print("=== Initializing Raster Layer ===")
    raster = MockRasterDataset()
    
    print(f"Raster Dimensions : Width={raster.width}, Height={raster.height}")
    print(f"Band Count        : {raster.count} (Multi-band spatial tensor)")
    print(f"Coordinate System : {raster.crs}")
    print(f"Geographic Bounds : {raster.bounds}")
    
    print("\nWhy this matters:")
    print("In later modules, these dimensions form your PyTorch tensor shape (B, C, H, W)")
    print("and the bounds/CRS allow you to convert pixel masks into real-world vectors!")

if __name__ == "__main__":
    inspect_raster()
    print("\nDay 3 status: SUCCESS!")

    