import streamlit as st

st.title("YUPI you chose Pizza!")

st.markdown("""
# 🍕 Homemade Pizza Recipe

### Ingredients
**For the dough:**
- 500 g flour (about 4 cups)
- 1 tsp salt  
- 1 tsp sugar  
- 7 g dry yeast (1 packet)  
- 300 ml warm water  
- 2 tbsp olive oil  

**For the topping:**
- 200 ml tomato sauce  
- 200 g mozzarella cheese, shredded  
- Fresh basil leaves  
- Olive oil  
- Salt & pepper  
- Optional: pepperoni, mushrooms, olives, bell peppers, onions

### Instructions

1. **Prepare the dough**  
   In a bowl, mix warm water, sugar, and yeast. Let it sit for 5–10 minutes until foamy.

2. **Mix ingredients**  
   Add flour, salt, and olive oil. Mix until a dough forms.

3. **Knead & rise**  
   Knead for 8–10 minutes until smooth. Cover and let rise for 1 hour, or until doubled in size.

4. **Preheat oven**  
   Preheat oven to 220°C (430°F). If you have a pizza stone, heat it too.

5. **Shape the pizza**  
   Roll out the dough on a floured surface to your desired thickness.

6. **Add toppings**  
   Spread tomato sauce, add mozzarella, and your favorite toppings.

7. **Bake**  
   Bake for 12–15 minutes, until crust is golden and cheese is bubbly.

8. **Finish**  
   Add fresh basil, drizzle with olive oil, slice, and enjoy!
""")


if st.button("Back to home"):
    st.switch_page("web.py")