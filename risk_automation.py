import pandas as pd
from openpyxl import load_workbook

# Define the file name
file_name = 'Risk register _upload.xlsx' 

try:
    print("⏳ Starting process... Please ensure the Excel file is closed.")
    
    # 1. LOAD DATA: Read the master data from the 'current' sheet
    # Pandas reads this top-to-bottom, preserving the original row order
    df_main = pd.read_excel(file_name, sheet_name='current')
    
    # 2. LOAD WORKBOOK: Open the existing file to access the blank sheets
    book = load_workbook(file_name)
    
    # 3. SET UP WRITER: Using 'overlay' mode to write into existing sheets 
    # without deleting them or changing their tab colors/names.
    with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        # Link the loaded workbook to the writer (Fix for 'no setter' error)
        writer._book = book 
        
        # List of ISO sheets we want to populate
        iso_sheets = ['9001', '14001', '27001', '45001']
        
        for std in iso_sheets:
            # FILTERING: Find rows where the 'ISO Standard' column contains the current number (e.g., '9001')
            filtered_df = df_main[df_main['ISO Standard'].astype(str).str.contains(std, na=False)]
            
            # MAPPING: Create a new structure that matches your blank sheet columns
            # This part maintains the left-to-right sequence of your columns
            mapped_data = pd.DataFrame()
            mapped_data['Source Reference ID'] = filtered_df['Source Reference ID']
            mapped_data['Title'] = filtered_df['Title']
            mapped_data['Description'] = filtered_df['Risk Description']
            mapped_data['Likelihood (1-5)'] = filtered_df['Likelihood']
            mapped_data['Impact (1-5)'] = filtered_df['Impact']
            mapped_data['Owner'] = filtered_df['Owner']
            mapped_data['Department'] = filtered_df['Department']
            mapped_data['Migitation Actions'] = filtered_df['Mitigating Action']
            mapped_data['Contingent Actions'] = filtered_df['Contingent Action']
            mapped_data['Progress on actions'] = filtered_df['Progress on Actions']
            mapped_data['Residual Risk'] = filtered_df['Residual Risk']

            # EXPORT: Write the mapped data to the specific sheet
            # index=False ensures Python doesn't add an extra column of numbers at the start
            mapped_data.to_excel(writer, sheet_name=std, index=False)
            print(f"✅ ISO {std} sheet updated successfully.")

        # 4. FINANCE RISKS: Logic to identify Finance-related risks
        def check_fin(row):
            # Combine Title and Description, then look for keywords in lowercase
            text = (str(row['Title']) + " " + str(row['Risk Description'])).lower()
            return 'finance' in text or 'accounts' in text

        # Apply the finance filter logic
        fin_df = df_main[df_main.apply(check_fin, axis=1)]
        
        # Mapping for Finance sheet
        fin_mapped = pd.DataFrame()
        fin_mapped['Source Reference ID'] = fin_df['Source Reference ID']
        fin_mapped['Title'] = fin_df['Title']
        fin_mapped['Description'] = fin_df['Risk Description']
        fin_mapped['Likelihood (1-5)'] = fin_df['Likelihood']
        fin_mapped['Impact (1-5)'] = fin_df['Impact']
        fin_mapped['Owner'] = fin_df['Owner']
        
        # Write to Finance risks sheet
        fin_mapped.to_excel(writer, sheet_name='Finance risks', index=False)
        print("✅ Finance risks sheet updated successfully.")

    print("\n🎉 Success! All data has been processed and implemented.")

except Exception as e:
    # This block catches any errors and tells you exactly what went wrong
    print(f"❌ Error encountered: {e}")