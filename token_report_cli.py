import argparse
import asyncio
import aiohttp
from spl_token_analysis import get_token_details_async
from spl_report_generator import create_pdf
import os
import tempfile

async def generate_report(token_address: str, output_dir: str = None):
    """Generate a security report for a given token address"""
    
    if not output_dir:
        output_dir = os.getcwd()
    
    async with aiohttp.ClientSession() as session:
        # Get token details
        token_details, _ = await get_token_details_async(token_address, session)
        
        if isinstance(token_details, str):
            print(f"Error: {token_details}")
            return
            
        # Add reviewer information
        result_dict = token_details.to_dict()
        result_dict['reviewer_name'] = 'SPL-AUTOMATION'
        result_dict['confirmation_status'] = 'Confirmed'
        
        # Generate PDF report
        try:
            pdf_path = create_pdf(result_dict, output_dir)
            print(f"\nReport generated successfully: {pdf_path}")
        except Exception as e:
            print(f"Error generating PDF report: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate Solana Token Security Report')
    parser.add_argument('address', help='Solana token address')
    parser.add_argument('--output', '-o', help='Output directory for the report (optional)')
    
    args = parser.parse_args()
    
    print(f"\nGenerating security report for token: {args.address}")
    
    asyncio.run(generate_report(args.address, args.output))

if __name__ == "__main__":
    main()