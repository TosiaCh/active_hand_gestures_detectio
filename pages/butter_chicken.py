import streamlit as st
st.title("Butter Chicken!")
st.markdown("""
# 🍛 Butter Chicken Recipe

### Ingredients
**For the chicken:**
- 500 g chicken, cut into pieces
- 2 tbsp butter
- 1 tsp ginger-garlic paste
- 1 tsp red chili powder
- Salt to taste

**For the sauce:**
- 200 ml heavy cream
- 1 tbsp garam masala
- 1 tbsp coriander powder
- 2 tbsp sugar
- Salt to taste

### Instructions

1. **Marinate chicken**  
   Mix chicken with ginger-garlic paste, chili powder, and salt. Let it marinate for 30 minutes.

2. **Cook chicken**  
   Heat butter in a pan and cook marinated chicken until golden brown.

3. **Make sauce**  
   Add cream, garam masala, coriander powder, and sugar to the pan. Simmer for 10 minutes.

4. **Serve**  
   Serve hot with naan or rice.
""")

if st.button("Back to home"):
    st.switch_page("web.py")