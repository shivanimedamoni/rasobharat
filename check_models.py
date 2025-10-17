import google.generativeai as genai

# Make sure your API key is set first
genai.configure(api_key="AIzaSyDnokIFNYFsm6VAa8bRVHBo-MLIR2NpE7I")  # replace with your actual API key

models = genai.list_models()
for model in models:
    print(model["name"], "supports:", model.get("capabilities", "unknown"))