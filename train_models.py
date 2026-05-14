"""
Script to train both ML models and populate ChromaDB from your dataset
Run this once before starting the Streamlit app
"""
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from server.models.classification_model import StartupClassifier
from server.models.funding_predictor import FundingPredictor
from server.services.rag_service import rag_service
from config import Config
import os

def train_all_models():
    print("\n" + "="*80)
    print("🎓 TRAINING ML MODELS FOR STARTUP IDEA HELPER PLATFORM")
    print("="*80 + "\n")
    
    # Ensure directories exist
    os.makedirs(Config.MODELS_DIR, exist_ok=True)
    os.makedirs(Config.CHROMA_DIR, exist_ok=True)
    
    # 1. Train Classification Model
    print("\n📊 STEP 1: Training Classification Model...")
    print("-"*80)
    classifier = StartupClassifier()
    
    if not os.path.exists(Config.LABELED_DATASET):
        print(f"❌ Error: Dataset not found at {Config.LABELED_DATASET}")
        print("💡 Please ensure 'startups_labeled_percentile.csv' is in the data/ folder")
        return False
    
    try:
        accuracy = classifier.train(Config.LABELED_DATASET)
        classifier.save(Config.CLASSIFIER_PATH)
        print(f"✅ Classification Model trained with {accuracy:.2%} accuracy\n")
    except Exception as e:
        print(f"❌ Classification training failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False
    
    # 2. Train Funding Predictor Model
    print("\n💰 STEP 2: Training Funding Predictor Model...")
    print("-"*80)
    predictor = FundingPredictor()
    
    if not os.path.exists(Config.FUNDING_DATASET):
        print(f"❌ Error: Dataset not found at {Config.FUNDING_DATASET}")
        print("💡 Please ensure 'startups_new_2.csv' is in the data/ folder")
        return False
    
    try:
        r2_score = predictor.train(Config.FUNDING_DATASET)
        predictor.save(
            Config.FUNDING_PREDICTOR_PATH,
            Config.SCALER_PATH,
            Config.FEATURES_PATH
        )
        print(f"✅ Funding Predictor trained with {r2_score:.2%} R² score\n")
    except Exception as e:
        print(f"❌ Funding predictor training failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False
    
    # 3. Populate ChromaDB from your dataset
    print("\n🗄️ STEP 3: Populating ChromaDB from Your Dataset...")
    print("-"*80)
    try:
        rag_service.populate_from_dataset(Config.FUNDING_DATASET, max_entries=500)
        count = rag_service.collection.count() if rag_service.collection else 0
        print(f"✅ ChromaDB populated with {count} startups from your dataset\n")
    except Exception as e:
        print(f"❌ ChromaDB population failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Summary
    print("\n" + "="*80)
    print("✅ MODEL TRAINING COMPLETE!")
    print("="*80)
    print("\nSaved Models:")
    print(f"  ✓ {Config.CLASSIFIER_PATH}")
    print(f"  ✓ {Config.FUNDING_PREDICTOR_PATH}")
    print(f"  ✓ {Config.SCALER_PATH}")
    print(f"  ✓ {Config.FEATURES_PATH}")
    print(f"\nChromaDB Location:")
    print(f"  ✓ {Config.CHROMA_DIR}")
    print(f"  ✓ Total startups indexed: {count}")
    print("\n💡 You can now run: streamlit run streamlit_app.py")
    print("="*80 + "\n")
    
    return True

if __name__ == "__main__":
    success = train_all_models()
    exit(0 if success else 1)