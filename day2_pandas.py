# Day 2: Pandas DataFrames for Spatial Metadata Tracking

import pandas as pd

def analyze_spatial_tiles():
    # 1. Create a dictionary simulating a catalog of satellite/drone GeoTIFF tiles
    data = {
        "tile_id": ["Tile_01", "Tile_02", "Tile_03", "Tile_04", "Tile_05"],
        "region": ["Vicgrid_A", "Vicgrid_A", "Vicgrid_B", "Vicgrid_B", "Vicgrid_A"],
        "area_sq_m": [12500.5, 43200.0, 8900.2, 51200.8, 15300.0],
        "cloud_cover_pct": [2.5, 14.1, 0.5, 45.2, 3.1],
        "processed": [True, True, True, False, True]
    }

    # 2. Convert dictionary into a Pandas DataFrame (our spreadsheet table)
    df = pd.DataFrame(data)

    print("=== Full Spatial Catalog ===")
    print(df)
    print("\n" + "="*40 + "\n")

    # 3. Filtering Data: Keep only tiles with less than 5% cloud cover AND are processed
    clean_tiles = df[(df["cloud_cover_pct"] < 5.0) & (df["processed"] == True)]
    
    print("=== Filtered High-Quality Tiles (< 5% Cloud) ===")
    print(clean_tiles)
    print("\n" + "="*40 + "\n")

    # 4. Aggregation: Calculate average area across regions
    avg_area = df.groupby("region")["area_sq_m"].mean()
    
    print("=== Average Tile Area by Region (m^2) ===")
    print(avg_area)

if __name__ == "__main__":
    analyze_spatial_tiles()
    print("\nDay 2 status: SUCCESS!")