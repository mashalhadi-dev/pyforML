# class Dataprocessor:
#     def __init__(self, dataset_name):
#         self.dataset_name = dataset_name
#         self.is_cleaned= False
#     def clean_data(self, raw_data):
#         cleaned = [item.strip().lower() for item in raw_data if item]
#         self.is_cleaned= True 
#         return cleaned
# processor = Dataprocessor("naame")
# print("Dataset Name:", processor.dataset_name)

# cleaned_result = processor.clean_data(["Ali", "", "SARA"])
# print("Cleaned Data:", cleaned_result)

# class ModelTrainer:
#     def __init__(self,model_name):
#         self.model_name = model_name
#         self.is_trained= False
#     def train_model(self, epochs):
#         print(f"Training {self.model_name} for {epochs} epochs...")
#         self.is_trained= True

# trainer = ModelTrainer("AI_Brain")
# trainer.train_model(5)
# print("Kya model train ho gaya?", trainer.is_trained)
