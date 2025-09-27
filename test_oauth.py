#!/usr/bin/env python3
"""
Simple OAuth test script to verify Google OAuth credentials are working
Run this after setting up your Google OAuth credentials in .env file
"""

import os
from dotenv import load_dotenv

def test_oauth_setup():
    """Test if OAuth credentials are properly configured"""
    
    print("🔍 Testing Google OAuth Setup...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ ERROR: .env file not found!")
        print("   Please create .env file with your Google OAuth credentials")
        return False
    
    # Check OAuth credentials
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    print(f"📁 .env file: ✅ Found")
    
    # Validate Client ID
    if not client_id or client_id == 'your_google_client_id_here':
        print("❌ GOOGLE_CLIENT_ID: Not configured")
        print("   Please set your real Google Client ID in .env file")
        return False
    else:
        # Mask the client ID for security
        masked_id = client_id[:20] + "..." + client_id[-20:] if len(client_id) > 40 else client_id
        print(f"✅ GOOGLE_CLIENT_ID: {masked_id}")
    
    # Validate Client Secret
    if not client_secret or client_secret == 'your_google_client_secret_here':
        print("❌ GOOGLE_CLIENT_SECRET: Not configured")
        print("   Please set your real Google Client Secret in .env file")
        return False
    else:
        # Mask the client secret for security
        masked_secret = client_secret[:8] + "..." + client_secret[-8:] if len(client_secret) > 16 else "***"
        print(f"✅ GOOGLE_CLIENT_SECRET: {masked_secret}")
    
    # Check if credentials look valid
    if not client_id.endswith('.apps.googleusercontent.com'):
        print("⚠️  WARNING: Client ID doesn't look like a valid Google Client ID")
        print("   Valid format: xxxxx.apps.googleusercontent.com")
        return False
    
    print("\n🎉 OAuth credentials look good!")
    print("\n📋 Next steps:")
    print("1. Make sure you've added these URLs to Google Cloud Console:")
    print("   - Authorized JavaScript origins: http://localhost:8000")
    print("   - Authorized redirect URIs: http://localhost:8000/auth/callback")
    print("2. Run: python app_with_auth.py")
    print("3. Open: http://localhost:8000")
    print("4. Test the Google login!")
    
    return True

if __name__ == "__main__":
    test_oauth_setup()
