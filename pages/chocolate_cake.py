import streamlit as st
st.title("Chocolate Cake!")
st.markdown("""
# 🍫 Chocolate Cake Recipe

### Ingredients
**For the cake:**
- 200 g flour (about 1.5 cups)
- 150 g sugar
- 100 g butter, melted
- 2 eggs
- 1 tsp vanilla extract
- 1 tsp baking powder
- 1/2 tsp salt

**For the frosting:**
- 100 g butter, softened
- 200 g powdered sugar
- 50 ml milk or cream
- 1 tsp vanilla extract

### Instructions

1. **Preheat oven**  
   Preheat oven to 180°C (350°F). Grease a cake pan.

2. **Mix ingredients**  
   In a bowl, mix melted butter, sugar, eggs, and vanilla. Add flour, baking powder, and salt.

3. **Bake**  
   Pour batter into the pan and bake for 30–35 minutes until a toothpick comes out clean.

4. **Make frosting**  
   Beat softened butter with powdered sugar and milk until smooth.

5. **Decorate & serve**  
   Spread frosting over the cooled cake and slice.
""")

if st.button("Back to home"):
    st.switch_page("web.py")