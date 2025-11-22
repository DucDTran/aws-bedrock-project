#!/usr/bin/env python3
"""
Test script for bedrock_utils.py functions
Usage: python test_bedrock.py
"""

from bedrock_utils import valid_prompt, query_knowledge_base, generate_response
import sys

def main():
    # Configuration - Update these values
    MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
    KB_ID = "8YSKIRMJZI"
    
    print("=" * 60)
    print("Testing Bedrock Utils Functions")
    print("=" * 60)
    
    # Test 1: valid_prompt
    print("\n1. Testing valid_prompt function...")
    test_prompts = [
        "What is the capacity of the excavator?",
        "How does the LLM work?",
        "Tell me about bulldozers"
    ]
    
    for prompt in test_prompts:
        print(f"\n   Prompt: '{prompt}'")
        is_valid = valid_prompt(prompt, MODEL_ID)
        print(f"   Valid: {is_valid}")
    
    if KB_ID is not None:
        print("\n2. Testing query_knowledge_base function...")
        query = "excavator specifications"
        print(f"   Query: '{query}'")
        results = query_knowledge_base(query, KB_ID)
        print(f"   Retrieved {len(results)} results")
        if results:
            print(f"   First result preview: {results[0]['content']['text'][:100]}...")
    else:
        print("\n2. Skipping query_knowledge_base test (KB_ID not set)")
    
    # Test 3: generate_response
    print("\n3. Testing generate_response function...")
    test_prompt = "What is the maximum capacity?"
    print(f"   Prompt: '{test_prompt}'")
    response = generate_response(
        test_prompt,
        MODEL_ID,
        temperature=0.7,
        top_p=0.9
    )
    print(f"   Response: {response[:200]}...")
    
    print("\n" + "=" * 60)
    print("Tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

