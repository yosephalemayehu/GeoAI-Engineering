# Day 1: Workspace Verification Script

def process_spatial_metadata():
    # Simulating a metadata dictionary from a GeoTIFF dataset
    layer_info = {
        "dataset_name": "Vicgrid_Region_A",
        "bands": 4,
        "resolution_meters": 0.5,
        "active": True
    }
    
    # Using modern Python f-strings to format output
    print(f"--- Loading Spatial Metadata ---")
    for key, value in layer_info.items():
        print(f"  {key.capitalize()}: {value}")

if __name__ == "__main__":
    process_spatial_metadata()
    print("\nEnvironment status: SUCCESS! Your Windows setup is ready.")