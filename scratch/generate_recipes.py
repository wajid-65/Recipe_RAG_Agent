import os

TEXT_DIR = r"c:\Users\ABDUL WAJID\Downloads\recipe_rag_agent_10\recipe_rag_agent\data\text_notes"

recipes = [
    # ── TAMIL NADU (10) ──────────────────────────────────────────────────────
    {
        "filename": "tn_sambar.md",
        "content": """# Authentic Tamil Nadu Sambar

Cuisine: Tamil Nadu, South Indian
Time: 40 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free

## Ingredients
- 1/2 cup toor dal (pigeon peas)
- 1 cup mixed vegetables (drumstick, carrots, pumpkin, pearl onions, eggplant)
- 1 medium tomato, chopped
- 1 tbsp tamarind paste dissolved in 1 cup warm water
- 2 tbsp Sambar powder
- 1/2 tsp turmeric powder
- 1/2 tsp asafoetida (hing)
- 1 tbsp sesame oil or ghee
- 1 tsp mustard seeds
- 1 tsp cumin seeds
- 2 dry red chilies
- 1 sprig curry leaves
- Salt to taste
- Fresh coriander leaves for garnish

## Instructions
1. Pressure cook toor dal with turmeric powder and 2 cups water for 4 whistles until soft. Mash smooth.
2. Cook mixed vegetables and chopped tomato in 1.5 cups water until tender (about 10 minutes).
3. Add tamarind water, sambar powder, asafoetida, and salt to the cooked vegetables. Simmer for 8 minutes until tamarind raw taste disappears.
4. Add the mashed dal and simmer for another 5 minutes on low heat. Adjust consistency with warm water if thick.
5. In a small pan, heat oil/ghee. Add mustard seeds, cumin seeds, dry red chilies, and curry leaves. Let them crackle.
6. Pour the tempering over the hot sambar. Garnish with chopped coriander and serve hot with steamed rice or idli.
"""
    },
    {
        "filename": "tn_chettinad_chicken.md",
        "content": """# Chettinad Spicy Chicken Curry

Cuisine: Tamil Nadu, Indian
Time: 50 minutes
Serves: 4
Diet tags: dairy-free, gluten-free, high-protein

## Ingredients
- 600g chicken, bone-in cut into medium pieces
- 2 large onions, finely sliced
- 2 tomatoes, chopped
- 1 sprig curry leaves
- 2 tbsp gingelly oil (sesame oil)
- 1 tsp ginger-garlic paste
- Salt to taste

### Chettinad Spice Powder (Roasted & Ground)
- 2 tbsp coriander seeds
- 1 tbsp fennel seeds
- 1 tbsp cumin seeds
- 1 tbsp black peppercorns
- 4 dry red chilies
- 1 star anise
- 2 cloves & 1 cinnamon stick
- 2 tbsp grated coconut

## Instructions
1. Dry roast coriander seeds, fennel, cumin, peppercorns, dry chilies, star anise, cloves, cinnamon, and grated coconut until fragrant. Cool and grind into a smooth paste with 3 tbsp water.
2. Heat gingelly oil in a heavy-bottomed pot. Add curry leaves and sliced onions. Sauté until deep golden brown.
3. Add ginger-garlic paste and stir for 2 minutes.
4. Add chopped tomatoes and cook until soft and oil separates.
5. Add chicken pieces, salt, and ground Chettinad spice paste. Stir well to coat chicken.
6. Cover and cook on medium heat for 15 minutes, allowing chicken to release its juices.
7. Add 1 cup of water, cover, and simmer for 20 minutes until chicken is tender and gravy thickens.
8. Garnish with fresh coriander and serve hot with parotta or steamed rice.
"""
    },
    {
        "filename": "tn_dosa_potato_masala.md",
        "content": """# Crispy Tamil Nadu Masala Dosa

Cuisine: Tamil Nadu, South Indian
Time: 30 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free

## Ingredients
- 3 cups fermented Dosa batter (rice and urad dal batter)
- Oil or ghee for roasting dosas

### Potato Masala Stuffing
- 4 medium potatoes, boiled, peeled, and coarsely mashed
- 1 large onion, thinly sliced
- 2 green chilies, finely chopped
- 1 tsp mustard seeds
- 1 tsp chana dal (split Bengal gram)
- 1/2 tsp turmeric powder
- 1/2 inch ginger, finely chopped
- 1 sprig curry leaves
- 1 tbsp oil
- Salt to taste
- Chopped coriander leaves

## Instructions
1. Heat 1 tbsp oil in a pan. Add mustard seeds and chana dal. Sauté until dal turns golden.
2. Add curry leaves, green chilies, ginger, and sliced onions. Sauté until onions turn translucent.
3. Stir in turmeric powder and salt.
4. Add mashed potatoes and 1/4 cup water. Mix well and simmer on low heat for 4 minutes until potato masala is moist and combined. Garnish with coriander.
5. Heat a cast-iron tawa/griddle on medium-high. Grease lightly with oil, then sprinkle water to cool slightly.
6. Pour a ladleful of dosa batter in the center and spread outwards in circles into a thin crepe.
7. Drizzle 1 tsp oil/ghee around the edges. Cook until bottom turns golden brown and crispy.
8. Place 3 tbsp of potato masala in the center, fold dosa over, and serve hot with coconut chutney and sambar.
"""
    },
    {
        "filename": "tn_idli_coconut_chutney.md",
        "content": """# Soft Steamed Idli with Tamil Coconut Chutney

Cuisine: Tamil Nadu, South Indian
Time: 25 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free, low-fat

## Ingredients
- 4 cups fermented Idli batter (rice and urad dal)
- Oil for greasing idli plates

### Tamil Style Coconut Chutney
- 1 cup fresh grated coconut
- 2 tbsp roasted chana dal (pottukadalai)
- 2 green chilies
- 1 small clove garlic
- 1/2 inch ginger
- Salt to taste
- 1/4 cup water

### Chutney Tempering
- 1 tsp oil
- 1/2 tsp mustard seeds
- 1 dry red chili
- 1 sprig curry leaves

## Instructions
1. Grease idli molds with a drop of oil. Pour fermented idli batter into each mold.
2. Steam in an idli cooker or steamer over high heat for 10-12 minutes until a toothpick inserted comes out clean. Rest for 2 minutes, then spoon out idlis.
3. For chutney: Blend grated coconut, roasted chana dal, green chilies, garlic, ginger, salt, and water into a smooth paste. Transfer to a bowl.
4. Heat 1 tsp oil in a small pan. Add mustard seeds, red chili, and curry leaves. Let crackle.
5. Pour tempering over coconut chutney and serve fresh alongside warm fluffy idlis.
"""
    },
    {
        "filename": "tn_kothu_parotta.md",
        "content": """# Madurai Street Style Chicken Kothu Parotta

Cuisine: Tamil Nadu, Indian
Time: 30 minutes
Serves: 2
Diet tags: high-protein

## Ingredients
- 4 cooked layered parottas, chopped into small pieces
- 1 cup cooked spicy chicken curry with gravy
- 2 eggs
- 1 large onion, finely chopped
- 1 tomato, finely chopped
- 2 green chilies, chopped
- 1 sprig curry leaves
- 1 tsp ginger-garlic paste
- 1/2 tsp chili powder
- 1/2 tsp garam masala
- 2 tbsp oil
- Salt and pepper to taste
- Fresh cilantro for garnish

## Instructions
1. Heat oil on a flat cast-iron griddle or large pan over high heat.
2. Add curry leaves, green chilies, and onions. Sauté until onions are translucent.
3. Add ginger-garlic paste and tomatoes. Cook until soft.
4. Crack 2 eggs onto the griddle and scramble quickly into the onion mixture.
5. Add chopped parotta pieces, chili powder, garam masala, and salt.
6. Pour chicken curry along with chicken pieces over the parotta mixture.
7. Using two flat metal spatulas or heavy bench scrapers, chop and mince the parotta rapidly against the iron griddle while mixing everything together for 5-7 minutes.
8. Garnish with chopped coriander and serve hot with onion raita.
"""
    },
    {
        "filename": "tn_medu_vada.md",
        "content": """# Crispy Tamil Medu Vada

Cuisine: Tamil Nadu, South Indian
Time: 35 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free

## Ingredients
- 1 cup whole white urad dal (soaked for 3 hours)
- 1 tbsp rice flour
- 1 green chili, finely chopped
- 1/2 inch ginger, finely chopped
- 1 sprig curry leaves, chopped
- 1 tsp black peppercorns, coarsely crushed
- 1 pinch asafoetida (hing)
- Salt to taste
- Oil for deep frying

## Instructions
1. Drain soaked urad dal thoroughly. Grind in a blender using minimal cold water (2-3 tbsp) into a thick, fluffy batter.
2. Transfer batter to a bowl. Beat vigorously with hands for 3 minutes to incorporate air.
3. Mix in rice flour, green chili, ginger, curry leaves, crushed peppercorns, hing, and salt.
4. Heat oil in a deep frying pan over medium heat.
5. Wet your palms with water. Take a small lemon-sized portion of batter, flatten slightly, and make a hole in the center with your thumb.
6. Gently drop shaped vada into hot oil. Fry on medium heat, turning occasionally, until golden brown and crispy (about 5-6 minutes).
7. Drain on paper towels and serve piping hot with coconut chutney and sambar.
"""
    },
    {
        "filename": "tn_chicken_65.md",
        "content": """# Chennai Hotel Style Chicken 65

Cuisine: Tamil Nadu, Indian
Time: 35 minutes
Serves: 4
Diet tags: gluten-free, high-protein

## Ingredients
- 500g boneless chicken, cut into bite-sized cubes
- 2 tbsp cornstarch
- 1 tbsp rice flour
- 1 egg white
- 1 tbsp ginger-garlic paste
- 1 tbsp Kashmiri red chili powder
- 1/2 tsp black pepper powder
- 1/2 tsp cumin powder
- 2 tbsp plain thick yogurt (curd)
- 1 tbsp lemon juice
- Salt to taste
- Oil for deep frying

### For Tempering
- 1 tbsp oil
- 2 sprigs curry leaves
- 3 green chilies, slit lengthwise
- 3 garlic cloves, sliced

## Instructions
1. Marinate chicken with ginger-garlic paste, chili powder, pepper, cumin powder, yogurt, lemon juice, salt, egg white, cornstarch, and rice flour for 30 minutes.
2. Heat oil in a pan for deep frying over medium-high heat.
3. Fry chicken pieces in batches for 5-6 minutes until crisp and cooked through. Drain on paper towels.
4. In a separate skillet, heat 1 tbsp oil. Add sliced garlic, slit green chilies, and curry leaves. Sauté for 1 minute until crisp.
5. Toss fried chicken pieces in the hot tempering for 1 minute and serve immediately with lemon wedges.
"""
    },
    {
        "filename": "tn_ven_pongal.md",
        "content": """# Classic Tamil Ven Pongal

Cuisine: Tamil Nadu, South Indian
Time: 30 minutes
Serves: 4
Diet tags: vegetarian, gluten-free

## Ingredients
- 1 cup raw rice (ponni rice or short grain rice)
- 1/2 cup yellow mung dal (split yellow lentils)
- 4 cups water
- 1 cup milk (optional, for extra richness)
- Salt to taste

### For Tempering
- 3 tbsp ghee
- 1 tsp cumin seeds
- 1 tsp black peppercorns, crushed
- 1/2 inch ginger, finely grated
- 10 cashews, halved
- 1 sprig curry leaves
- 1 pinch asafoetida (hing)

## Instructions
1. Dry roast yellow mung dal in a pan on medium heat for 3 minutes until aromatic. Wash rice and dal together.
2. In a pressure cooker, combine washed rice, mung dal, 4 cups water, 1 cup milk, and salt. Cook for 4-5 whistles until very soft and mushy.
3. Once pressure releases naturally, open cooker and mash the pongal gently with a spatula.
4. Heat ghee in a small pan. Add cashews and fry until golden. Remove cashews and set aside.
5. In the same hot ghee, add cumin seeds, crushed black peppercorns, grated ginger, curry leaves, and asafoetida. Let sizzle for 30 seconds.
6. Pour tempering and fried cashews into mashed pongal. Mix thoroughly and serve warm with coconut chutney and sambar.
"""
    },
    {
        "filename": "tn_tomato_rasam.md",
        "content": """# Tamil Nadu Pepper Tomato Rasam

Cuisine: Tamil Nadu, South Indian
Time: 20 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free, low-fat

## Ingredients
- 2 ripe tomatoes, coarsely chopped
- 1 tbsp tamarind paste in 1.5 cups warm water
- 1/2 tsp turmeric powder
- 1 pinch asafoetida (hing)
- 2 cups water
- Salt to taste
- Fresh cilantro for garnish

### Rasam Spice Powder (Crushed Coarsely)
- 1 tbsp black peppercorns
- 1 tbsp cumin seeds
- 4 garlic cloves

### Tempering
- 1 tbsp ghee or oil
- 1 tsp mustard seeds
- 1 dry red chili
- 1 sprig curry leaves

## Instructions
1. Coarsely crush black peppercorns, cumin seeds, and garlic together in a mortar and pestle.
2. In a pot, combine tamarind water, chopped tomatoes, turmeric, asafoetida, crushed spice mixture, and salt.
3. Simmer over medium heat for 10 minutes until tomatoes are completely soft and tamarind raw flavor disappears.
4. Add 2 cups water and bring to a gentle simmer. Cook just until frothy on top (do not let rasam boil rapidly).
5. Heat ghee/oil in a small pan. Add mustard seeds, red chili, and curry leaves. Let crackle.
6. Pour tempering into rasam, garnish generously with cilantro, cover immediately with a lid, and serve as soup or with rice.
"""
    },
    {
        "filename": "tn_fish_fry.md",
        "content": """# Tamil Nadu Spicy Pan-Fried Fish

Cuisine: Tamil Nadu, Indian
Time: 25 minutes
Serves: 3
Diet tags: dairy-free, gluten-free, high-protein, keto, low-carb

## Ingredients
- 500g fish steaks (Seer fish/Kingfish or Pomfret)
- 1 tbsp Kashmiri red chili powder
- 1/2 tsp turmeric powder
- 1 tsp coriander powder
- 1 tsp fennel seed powder
- 1/2 tsp black pepper powder
- 1 tbsp ginger-garlic paste
- 1 tbsp lemon juice
- 1 tbsp rice flour (for crispiness)
- Salt to taste
- 3 tbsp coconut oil or gingelly oil for shallow frying
- Curry leaves for garnish

## Instructions
1. Clean and pat dry fish steaks with paper towels.
2. In a bowl, mix red chili powder, turmeric, coriander powder, fennel powder, pepper, ginger-garlic paste, lemon juice, rice flour, salt, and 1 tbsp water into a thick spice paste.
3. Rub marinade evenly over fish steaks. Rest for 20 minutes.
4. Heat coconut oil in a wide skillet over medium heat. Add a sprig of curry leaves into the oil.
5. Place fish steaks in the pan and shallow fry for 4-5 minutes on medium heat until golden brown.
6. Flip carefully and fry the other side for another 4 minutes until cooked through and crispy.
7. Serve hot with onion rings and lemon wedges.
"""
    },

    # ── REST OF INDIA (10) ───────────────────────────────────────────────────
    {
        "filename": "in_chana_masala.md",
        "content": """# Punjabi Chana Masala

Cuisine: Indian
Time: 40 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free, high-protein

## Ingredients
- 2 cups cooked chickpeas (canned or soaked overnight and boiled)
- 2 tbsp oil
- 1 tsp cumin seeds
- 1 large onion, finely chopped
- 1 tbsp ginger-garlic paste
- 2 tomatoes, pureed
- 1 tbsp Chana Masala powder
- 1 tsp coriander powder
- 1/2 tsp turmeric powder
- 1 tsp red chili powder
- 1/2 tsp amchur (dry mango powder)
- 1 tsp kasuri methi (dried fenugreek leaves)
- Salt to taste
- Fresh cilantro for garnish

## Instructions
1. Heat oil in a pan. Add cumin seeds and let them crackle.
2. Add chopped onions and sauté until golden brown (about 7 minutes).
3. Add ginger-garlic paste and sauté for 1 minute until raw aroma goes away.
4. Add tomato puree, chana masala powder, coriander powder, turmeric, red chili powder, and salt. Cook until oil separates from gravy.
5. Add cooked chickpeas and 1 cup of chickpea cooking water. Coarsely mash a few chickpeas with the back of a spoon to thicken gravy.
6. Simmer covered for 15 minutes on low heat.
7. Stir in amchur powder and crushed kasuri methi.
8. Garnish with chopped cilantro and sliced ginger. Serve hot with bhature or basmati rice.
"""
    },
    {
        "filename": "in_palak_paneer.md",
        "content": """# Creamy Palak Paneer

Cuisine: Indian
Time: 35 minutes
Serves: 4
Diet tags: vegetarian, gluten-free, high-protein

## Ingredients
- 300g spinach leaves (palak), washed
- 250g paneer (Indian cottage cheese), cubed
- 2 tbsp ghee or butter
- 1 tsp cumin seeds
- 1 large onion, finely chopped
- 1 tbsp ginger-garlic paste
- 2 green chilies
- 1 tomato, finely chopped
- 1/2 tsp turmeric powder
- 1 tsp coriander powder
- 1/2 tsp garam masala
- 3 tbsp heavy cream
- Salt to taste

## Instructions
1. Blanch spinach leaves in boiling water for 2 minutes. Transfer immediately to ice water to retain vibrant green color. Drain and blend into a smooth puree with green chilies.
2. Heat 1 tbsp ghee in a pan and lightly sear paneer cubes for 2 minutes until light golden. Set aside in warm water.
3. Heat remaining ghee in the pan. Add cumin seeds and let sizzle.
4. Add onions and cook until translucent. Add ginger-garlic paste and sauté 1 minute.
5. Add chopped tomato, turmeric, coriander powder, and salt. Cook until tomatoes soften.
6. Pour in spinach puree and stir well. Simmer on low heat for 5 minutes.
7. Add paneer cubes, garam masala, and heavy cream. Simmer gently for 3 minutes.
8. Garnish with a drizzle of cream and serve hot with garlic naan or roti.
"""
    },
    {
        "filename": "in_hyderabadi_biryani.md",
        "content": """# Hyderabadi Vegetable Dum Biryani

Cuisine: Indian
Time: 60 minutes
Serves: 6
Diet tags: vegetarian, gluten-free

## Ingredients
- 2 cups Aged Basmati Rice (soaked 30 mins)
- 2 cups mixed vegetables (carrots, beans, peas, potatoes, cauliflower)
- 1 cup thick yogurt (curd)
- 2 large onions, thinly sliced and deep-fried until golden (birista)
- 1/4 cup mint leaves, chopped
- 1/4 cup fresh coriander, chopped
- 3 tbsp ghee
- Whole spices: 2 bay leaves, 4 cardamom pods, 4 cloves, 1 cinnamon stick, 1 tsp star anise
- 1 tbsp ginger-garlic paste
- 1 tbsp Biryani Masala powder
- 1/2 tsp red chili powder
- 1/2 tsp turmeric powder
- 1 pinch saffron strands soaked in 3 tbsp warm milk
- Salt to taste

## Instructions
1. Boil 8 cups of water with whole spices and salt. Add soaked rice and cook until 70% done (about 5 minutes). Drain rice.
2. In a heavy bottom pot, mix vegetables, yogurt, half fried onions, ginger-garlic paste, biryani masala, chili powder, turmeric, mint, coriander, 1 tbsp ghee, and salt. Marinate 15 minutes.
3. Spread marinated vegetables evenly at the bottom of the pot.
4. Layer cooked rice over vegetables. Top with remaining fried onions, mint, cilantro, saffron milk, and melted ghee.
5. Seal pot tightly with foil or dough lid. Cook on medium heat for 5 minutes, then place pot on a tawa (griddle) on low heat for 25 minutes (Dum cooking).
6. Rest sealed for 10 minutes. Fluff gently and serve with cucumber raita.
"""
    },
    {
        "filename": "in_pav_bhaji.md",
        "content": """# Mumbai Street Style Pav Bhaji

Cuisine: Indian
Time: 40 minutes
Serves: 4
Diet tags: vegetarian

## Ingredients
- 3 potatoes, boiled and mashed
- 1 cup cauliflower florets, boiled and mashed
- 1/2 cup green peas, boiled and mashed
- 1 bell pepper (capsicum), finely chopped
- 2 large onions, finely chopped
- 3 tomatoes, finely chopped
- 1 tbsp ginger-garlic paste
- 2 tbsp Pav Bhaji masala
- 1 tsp Kashmiri red chili powder (for red color)
- 1/2 tsp turmeric powder
- 4 tbsp butter
- 1 tbsp lemon juice
- 8 Pav buns
- Salt to taste
- Chopped cilantro and red onions for serving

## Instructions
1. Boil potatoes, cauliflower, and green peas together until soft. Mash completely.
2. Heat 2 tbsp butter in a large flat tava or skillet. Add chopped onions and ginger-garlic paste. Sauté until golden.
3. Add capsicum and tomatoes. Cook until tomatoes turn mushy and oil/butter separates.
4. Add pav bhaji masala, Kashmiri chili powder, turmeric, and salt. Mix well.
5. Add mashed boiled vegetables and 1/2 cup water. Mash continuously with a potato masher on the skillet while simmering for 10 minutes.
6. Stir in 1 tbsp butter and lemon juice.
7. Slit pav buns horizontally. Toast on a warm skillet with generous butter and cilantro until crisp and warm.
8. Serve hot bhaji topped with a knob of butter alongside butter-toasted pav, chopped onions, and lemon wedges.
"""
    },
    {
        "filename": "in_dal_makhani.md",
        "content": """# Restaurant Style Dal Makhani

Cuisine: Indian
Time: 70 minutes
Serves: 6
Diet tags: vegetarian, gluten-free, high-protein

## Ingredients
- 1 cup whole black lentils (sabut urad dal), soaked overnight
- 1/4 cup kidney beans (rajma), soaked overnight
- 4 cups water
- 3 tbsp butter
- 1 tbsp ghee
- 1 tsp cumin seeds
- 1 tbsp ginger-garlic paste
- 1 cup fresh tomato puree
- 1/2 tsp turmeric powder
- 1 tsp Kashmiri red chili powder
- 1/2 tsp garam masala
- 1/2 cup heavy cream
- Salt to taste

## Instructions
1. Pressure cook soaked black lentils and kidney beans with 4 cups water and salt for 8-10 whistles until soft. Mash slightly with a spoon.
2. Heat butter and ghee in a heavy pot. Add cumin seeds and sizzle.
3. Add ginger-garlic paste and cook for 1 minute. Add tomato puree, red chili powder, and turmeric. Cook until butter separates from masala.
4. Pour cooked lentils and beans into tomato gravy along with cooking liquid. Mix thoroughly.
5. Simmer on low heat for 40-45 minutes, stirring occasionally and adding water as needed to reach a creamy consistency.
6. Stir in garam masala and heavy cream. Cook another 5 minutes.
7. Serve piping hot garnished with butter and cream alongside naan or jeera rice.
"""
    },
    {
        "filename": "in_chole_bhature.md",
        "content": """# Delhi Style Chole Bhature

Cuisine: Indian
Time: 50 minutes
Serves: 4
Diet tags: vegetarian

## Ingredients
### For Chole (Chickpea Curry)
- 2 cups chickpeas, soaked overnight and pressure cooked with 1 tea bag and salt
- 2 tbsp oil
- 1 bay leaf, 1 black cardamom, 1 cinnamon stick
- 2 onions, pureed
- 1 tbsp ginger-garlic paste
- 2 tomatoes, pureed
- 2 tbsp Chole Masala
- 1 tsp coriander powder
- 1/2 tsp cumin powder
- 1 tsp red chili powder
- 1/2 tsp amchur (mango powder)
- Salt to taste

### For Bhature (Fried Bread)
- 2 cups all-purpose flour (maida)
- 2 tbsp semolina (sooji)
- 1/4 cup plain yogurt
- 1/2 tsp baking powder
- 1/2 tsp sugar
- Warm water to knead
- Oil for deep frying

## Instructions
1. Knead flour, semolina, yogurt, baking powder, sugar, salt, and warm water into a soft dough. Cover and rest for 2 hours.
2. For Chole: Heat oil with whole spices. Add onion puree and sauté until deep brown.
3. Add ginger-garlic paste and tomato puree. Cook until oil separates.
4. Stir in chole masala, coriander, cumin, chili powder, salt, cooked chickpeas, and 1 cup chickpea stock. Simmer 15 minutes until gravy thickens. Finish with amchur.
5. Divide bhatura dough into balls, roll into ovals.
6. Deep fry in hot oil until bhatura puffs up into a golden ball.
7. Serve hot bhature with spicy chole, pickled onions, and green chilies.
"""
    },
    {
        "filename": "in_rogan_josh.md",
        "content": """# Kashmiri Lamb Rogan Josh

Cuisine: Indian
Time: 65 minutes
Serves: 4
Diet tags: gluten-free, dairy-free, high-protein

## Ingredients
- 600g mutton or lamb shoulder, cut into pieces
- 4 tbsp mustard oil or ghee
- Whole spices: 2 bay leaves, 4 green cardamoms, 2 black cardamoms, 4 cloves, 1 inch cinnamon
- 1 tsp cumin seeds
- 1 tsp ginger powder (sonth)
- 1 tbsp fennel powder (saunf)
- 2 tbsp Kashmiri red chili powder (mixed with 3 tbsp water to form paste)
- 1/2 cup whisked yogurt
- 1 pinch asafoetida (hing)
- Salt to taste
- 1.5 cups mutton broth or water

## Instructions
1. Heat mustard oil in a heavy pot until smoking point. Cool slightly, then add whole spices, cumin seeds, and asafoetida.
2. Add lamb pieces and sear on high heat for 8 minutes until browned.
3. Lower heat and add chili paste, ginger powder, and fennel powder. Stir continuously for 2 minutes.
4. Add whisked yogurt gradually while stirring to prevent curdling. Cook until oil separates.
5. Add salt and 1.5 cups broth/water. Cover tightly and simmer on low heat for 45-50 minutes until lamb is melt-in-mouth tender.
6. Rest 10 minutes before serving with steamed basmati rice.
"""
    },
    {
        "filename": "in_aloo_gobi.md",
        "content": """# North Indian Aloo Gobi Dry Curry

Cuisine: Indian
Time: 30 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free, low-carb

## Ingredients
- 1 medium cauliflower, cut into florets
- 2 medium potatoes, peeled and cubed
- 2 tbsp mustard oil or vegetable oil
- 1 tsp cumin seeds
- 1/2 tsp turmeric powder
- 1 tsp coriander powder
- 1/2 tsp red chili powder
- 1/2 tsp garam masala
- 1 inch ginger, julienned
- 2 green chilies, slit
- 1 tomato, finely chopped
- Salt to taste
- Chopped fresh coriander

## Instructions
1. Heat oil in a pan. Add cumin seeds, julienned ginger, and green chilies. Sauté 30 seconds.
2. Add cubed potatoes, turmeric powder, and salt. Cover and cook on medium heat for 6 minutes.
3. Add cauliflower florets, chopped tomato, coriander powder, and red chili powder. Mix well.
4. Cover pan and cook on low heat for 12-15 minutes, stirring occasionally until potatoes and cauliflower are tender but firm (not mushy).
5. Sprinkle garam masala and fresh coriander. Stir gently on high heat for 1 minute to crisp edges slightly. Serve warm with roti.
"""
    },
    {
        "filename": "in_malai_kofta.md",
        "content": """# Shahi Malai Kofta

Cuisine: Indian
Time: 45 minutes
Serves: 4
Diet tags: vegetarian, high-protein

## Ingredients
### For Koftas (Dumplings)
- 1.5 cups paneer, grated
- 2 medium potatoes, boiled and mashed
- 2 tbsp cornstarch
- 1/4 cup cashews and raisins, chopped
- 1/2 tsp garam masala
- Salt to taste
- Oil for frying

### For Shahi Gravy
- 2 tbsp butter
- 1 tbsp oil
- 2 onions, chopped
- 3 tomatoes, chopped
- 10 cashews
- 1 inch ginger & 4 garlic cloves
- 1/2 tsp turmeric powder
- 1 tsp Kashmiri chili powder
- 1/2 tsp garam masala
- 1/4 cup heavy cream
- 1 tsp kasuri methi

## Instructions
1. For Koftas: Combine grated paneer, mashed potatoes, cornstarch, garam masala, and salt. Form into small balls stuffed with chopped cashews and raisins.
2. Deep fry koftas in medium-hot oil until golden brown. Drain on paper towels.
3. For Gravy: Boil onions, tomatoes, ginger, garlic, and cashews in 1 cup water for 10 minutes. Cool and blend to smooth paste.
4. Heat butter and oil in a pan. Add blended paste, turmeric, Kashmiri chili powder, and salt. Cook until butter separates.
5. Stir in cream, garam masala, and kasuri methi. Simmer 3 minutes.
6. Place fried koftas in a serving dish, pour rich warm gravy over them right before serving, and garnish with cream.
"""
    },
    {
        "filename": "in_dhokla.md",
        "content": """# Instant Gujarati Khaman Dhokla

Cuisine: Indian
Time: 25 minutes
Serves: 4
Diet tags: vegan, vegetarian, gluten-free, low-fat

## Ingredients
- 1.5 cups gram flour (besan)
- 1.5 tbsp semolina or rice flour
- 1 tbsp lemon juice
- 1 tbsp green chili-ginger paste
- 1/4 tsp turmeric powder
- 1 tbsp sugar
- 1 tsp fruit salt (Eno) or 3/4 tsp baking soda
- 1 tbsp oil
- 1 cup water
- Salt to taste

### Tempering
- 1 tbsp oil
- 1 tsp mustard seeds
- 1 tbsp sesame seeds
- 2 green chilies, slit
- 1 sprig curry leaves
- 1/4 cup water with 1 tsp sugar
- Fresh coconut and cilantro for garnish

## Instructions
1. Whisk besan, semolina, lemon juice, chili-ginger paste, turmeric, sugar, salt, oil, and 1 cup water into a smooth batter.
2. Prepare steamer with water. Grease a steaming pan with oil.
3. Add fruit salt (Eno) to batter and stir quickly in one direction for 10 seconds until batter turns light and frothy.
4. Pour immediately into greased pan and steam on high heat for 15 minutes. Cool slightly and cut into squares.
5. Heat oil for tempering. Add mustard seeds, sesame seeds, green chilies, and curry leaves. Add sugar water and bring to boil.
6. Pour sweet warm tempering evenly over cut dhokla squares. Garnish with fresh coconut and coriander.
"""
    },

    # ── AMERICA (10) ────────────────────────────────────────────────────────
    {
        "filename": "us_classic_cheeseburger.md",
        "content": """# Classic American Beef Cheeseburger

Cuisine: American
Time: 20 minutes
Serves: 2
Diet tags: high-protein

## Ingredients
- 300g ground beef chuck (80/20 fat ratio)
- 2 slices American cheddar cheese
- 2 brioche burger buns
- 2 tbsp butter
- 2 lettuce leaves
- 4 tomato slices
- 4 pickle slices
- 1/2 red onion, sliced into rings
- Salt and freshly cracked black pepper

### Burger Sauce
- 2 tbsp mayonnaise
- 1 tbsp ketchup
- 1 tsp yellow mustard
- 1/2 tsp dill pickle relish

## Instructions
1. Mix mayonnaise, ketchup, mustard, and pickle relish in a bowl to make secret burger sauce.
2. Divide ground beef into two loose 150g balls. Do not overwork meat.
3. Butter brioche buns and toast on a skillet until golden brown.
4. Heat a cast-iron skillet over high heat. Place beef balls on skillet and smash down flat with a heavy spatula.
5. Season generously with salt and pepper. Sear for 2 minutes until edges are crispy.
6. Flip patties, season again, and immediately top each patty with a slice of American cheddar. Cook 1 minute until melted.
7. Spread sauce on bottom buns, top with lettuce, tomato, cheesy beef patty, pickles, onion rings, top bun, and serve immediately.
"""
    },
    {
        "filename": "us_macaroni_and_cheese.md",
        "content": """# Baked Three-Cheese Macaroni and Cheese

Cuisine: American
Time: 40 minutes
Serves: 6
Diet tags: vegetarian, high-protein

## Ingredients
- 300g elbow macaroni
- 4 tbsp butter
- 1/4 cup all-purpose flour
- 3 cups whole milk, warm
- 2 cups sharp cheddar cheese, grated
- 1 cup Gruyere or Monterey Jack cheese, grated
- 1/2 cup Parmesan cheese, grated
- 1/2 tsp paprika
- 1/2 tsp garlic powder
- Salt and black pepper to taste
- 1/2 cup panko breadcrumbs mixed with 1 tbsp melted butter

## Instructions
1. Preheat oven to 375°F (190°C). Grease a 9x13 inch baking dish.
2. Cook elbow macaroni in salted boiling water for 2 minutes less than package instructions (al dente). Drain.
3. Melt butter in a saucepan over medium heat. Whisk in flour and cook 1-2 minutes until bubbling (roux).
4. Gradually whisk in warm milk. Cook for 5 minutes, whisking constantly until sauce thickens.
5. Remove from heat. Stir in paprika, garlic powder, salt, pepper, and 3/4 of the grated cheeses until smooth.
6. Fold cooked macaroni into cheese sauce. Pour into baking dish.
7. Top with remaining cheese and buttered panko breadcrumbs.
8. Bake for 20 minutes until top is golden brown and cheese sauce is bubbling.
"""
    },
    {
        "filename": "us_buffalo_chicken_wings.md",
        "content": """# Crispy Baked Buffalo Chicken Wings

Cuisine: American
Time: 45 minutes
Serves: 4
Diet tags: gluten-free, high-protein, keto, low-carb

## Ingredients
- 1kg chicken wings, split into flats and drumettes
- 1 tbsp aluminum-free baking powder
- 1 tsp garlic powder
- 1 tsp salt
- 1/2 tsp black pepper

### Buffalo Sauce
- 1/3 cup Frank's RedHot sauce or cayenne pepper sauce
- 4 tbsp unsalted butter, melted
- 1 tbsp honey or maple syrup (optional)
- 1/2 tsp Worcestershire sauce

### For Serving
- Celery sticks
- Blue cheese dip or ranch dressing

## Instructions
1. Preheat oven to 425°F (220°C). Line a baking sheet with foil and place a wire cooling rack on top.
2. Pat chicken wings completely dry with paper towels.
3. Toss wings with baking powder, garlic powder, salt, and pepper until evenly coated.
4. Arrange wings in a single layer on wire rack. Bake for 40-45 minutes, flipping halfway through, until skin is deep golden and ultra-crispy.
5. In a large bowl, whisk melted butter, hot sauce, honey, and Worcestershire sauce.
6. Add hot baked wings into buffalo sauce and toss thoroughly to coat.
7. Serve hot with celery sticks and cool blue cheese dipping sauce.
"""
    },
    {
        "filename": "us_new_england_clam_chowder.md",
        "content": """# Classic New England Clam Chowder

Cuisine: American
Time: 45 minutes
Serves: 4
Diet tags: high-protein

## Ingredients
- 4 slices thick-cut bacon, diced
- 2 tbsp butter
- 1 medium yellow onion, diced
- 2 celery stalks, diced
- 3 tbsp all-purpose flour
- 2 cups chicken stock or clam juice
- 2 cups Yukon Gold potatoes, peeled and cubed
- two 6.5 oz cans minced clams in juice (juice reserved)
- 1 cup heavy cream
- 1 bay leaf
- Salt and black pepper to taste
- Oyster crackers for serving

## Instructions
1. In a large Dutch oven, cook diced bacon over medium heat until crisp. Remove bacon with slotted spoon, leaving grease in pot.
2. Add butter, diced onion, and celery to bacon grease. Sauté for 5 minutes until soft.
3. Stir in flour and cook 1-2 minutes.
4. Slowly pour in reserved clam juice and chicken stock while stirring constantly to prevent lumps.
5. Add cubed potatoes and bay leaf. Bring to a simmer and cook 15 minutes until potatoes are tender.
6. Stir in heavy cream and minced clams. Simmer gently for 5 minutes (do not boil).
7. Remove bay leaf, season with salt and black pepper.
8. Ladle into warm bowls, top with crispy bacon and oyster crackers.
"""
    },
    {
        "filename": "us_bbq_pulled_pork.md",
        "content": """# Slow-Cooked Texas BBQ Pulled Pork

Cuisine: American
Time: 240 minutes
Serves: 8
Diet tags: dairy-free, gluten-free, high-protein

## Ingredients
- 1.5kg pork shoulder / pork butt
- 1 cup sweet BBQ sauce

### Dry Spice Rub
- 2 tbsp brown sugar
- 1 tbsp smoked paprika
- 1 tbsp garlic powder
- 1 tbsp onion powder
- 1 tsp cumin
- 1 tsp chili powder
- 1 tbsp salt
- 1 tsp black pepper
- 1/2 cup apple cider vinegar

## Instructions
1. Mix brown sugar, smoked paprika, garlic powder, onion powder, cumin, chili powder, salt, and pepper to make dry rub.
2. Rub dry spice mixture all over pork shoulder.
3. Place pork in a slow cooker or heavy Dutch oven. Pour apple cider vinegar around the base.
4. Cover and cook on LOW for 7-8 hours (or 3.5 hours at 300°F in oven) until pork is extremely tender and pulls apart easily with a fork.
5. Shred pork using two forks, discarding excess fat.
6. Toss shredded pork with sweet BBQ sauce and 1/2 cup cooking juices.
7. Serve piled high on toasted hamburger buns with coleslaw.
"""
    },
    {
        "filename": "us_ny_cheesecake.md",
        "content": """# Classic New York Baked Cheesecake

Cuisine: American
Time: 90 minutes
Serves: 10
Diet tags: vegetarian

## Ingredients
### Graham Cracker Crust
- 1.5 cups graham cracker crumbs
- 3 tbsp sugar
- 5 tbsp unsalted butter, melted

### Cheesecake Filling
- 900g (four 8oz blocks) cream cheese, softened to room temperature
- 1 cup granulated sugar
- 1 tbsp vanilla extract
- 1 cup sour cream
- 4 large eggs, room temperature
- 2 tbsp all-purpose flour

## Instructions
1. Preheat oven to 350°F (175°C). Wrap outside of a 9-inch springform pan with heavy duty foil.
2. Mix graham cracker crumbs, sugar, and melted butter. Press firmly into bottom of springform pan. Bake 10 minutes, then cool.
3. Beat softened cream cheese and sugar together until completely smooth and creamy (about 3 minutes).
4. Mix in vanilla extract, sour cream, and flour.
5. Add eggs one at a time on low speed, mixing just until combined.
6. Pour filling over cooled crust. Place springform pan in a large roasting pan filled with 1 inch of hot water (water bath).
7. Bake at 325°F (160°C) for 70 minutes until edges are set but center wobbles slightly.
8. Turn off oven, crack door open, and let cheesecake cool inside for 1 hour. Chill in refrigerator overnight before serving.
"""
    },
    {
        "filename": "us_fluffy_pancakes.md",
        "content": """# Fluffy American Buttermilk Pancakes

Cuisine: American
Time: 20 minutes
Serves: 4
Diet tags: vegetarian

## Ingredients
- 2 cups all-purpose flour
- 2 tbsp sugar
- 2 tsp baking powder
- 1/2 tsp baking soda
- 1/2 tsp salt
- 2 cups buttermilk
- 2 large eggs
- 4 tbsp melted butter, cooled
- 1 tsp vanilla extract
- Maple syrup and butter for serving

## Instructions
1. Whisk flour, sugar, baking powder, baking soda, and salt in a large bowl.
2. In a separate bowl, whisk buttermilk, eggs, melted butter, and vanilla extract.
3. Pour wet ingredients into dry ingredients and fold gently with a spatula just until combined (do not overmix; lumps are fine). Rest batter for 10 minutes.
4. Heat a non-stick griddle or pan over medium heat. Lightly butter the surface.
5. Pour 1/4 cup batter for each pancake. Cook for 2-3 minutes until bubbles form on top and edges look set.
6. Flip gently and cook another 1-2 minutes until golden brown.
7. Serve warm in stacks topped with a knob of butter and pure maple syrup.
"""
    },
    {
        "filename": "us_texas_chili.md",
        "content": """# Hearty Texas Beef Chili

Cuisine: American
Time: 90 minutes
Serves: 6
Diet tags: dairy-free, gluten-free, high-protein, low-carb

## Ingredients
- 1kg coarse ground beef or chuck roast diced small
- 2 tbsp bacon fat or oil
- 1 large yellow onion, diced
- 4 garlic cloves, minced
- 3 tbsp chili powder
- 1 tbsp cumin
- 1 tbsp smoked paprika
- 1 tsp dried oregano
- 2 cups beef broth
- 1 can (14 oz) crushed tomatoes
- 1 tbsp Worcestershire sauce
- Salt and black pepper
- Optional toppings: shredded cheddar, sour cream, sliced jalapenos

## Instructions
1. Heat oil/bacon fat in a heavy Dutch oven over medium-high heat.
2. Add beef in batches and sear until browned. Remove and set aside.
3. Add onion and garlic to pot, cook 5 minutes until soft.
4. Stir in chili powder, cumin, smoked paprika, and oregano. Cook 1 minute.
5. Return browned beef to pot. Add crushed tomatoes, beef broth, and Worcestershire sauce.
6. Bring to a boil, then reduce heat to low, cover, and simmer for 1 hour until beef is melt-in-mouth tender.
7. Uncover and simmer 15 minutes to thicken sauce. Season with salt and pepper.
8. Serve hot topped with shredded cheddar, sour cream, and jalapenos.
"""
    },
    {
        "filename": "us_apple_pie.md",
        "content": """# Traditional American Apple Pie

Cuisine: American
Time: 75 minutes
Serves: 8
Diet tags: vegetarian

## Ingredients
- 2 double pie crust sheets (chilled)
- 6 large apples (mix of Granny Smith and Honeycrisp), peeled, cored, and sliced
- 3/4 cup sugar
- 2 tbsp all-purpose flour
- 1 tsp cinnamon powder
- 1/4 tsp nutmeg powder
- 1 tbsp lemon juice
- 2 tbsp butter, cut into small cubes
- 1 egg beaten with 1 tbsp water (egg wash)

## Instructions
1. Preheat oven to 400°F (200°C).
2. Toss sliced apples with sugar, flour, cinnamon, nutmeg, and lemon juice in a large bowl.
3. Line a 9-inch pie dish with the bottom pie crust sheet.
4. Fill crust with apple mixture, mounding apples in the center. Dot top with butter cubes.
5. Place second pie crust over filling. Trim and crimp edges to seal crusts together. Cut 4 slits on top for steam vents.
6. Brush top crust with egg wash and sprinkle lightly with sugar.
7. Bake at 400°F for 20 minutes, then lower heat to 375°F (190°C) and bake 35 minutes until crust is deep golden and filling bubbles.
8. Cool 2 hours before slicing to allow juices to set. Serve warm with vanilla ice cream.
"""
    },
    {
        "filename": "us_cobb_salad.md",
        "content": """# Classic American Cobb Salad

Cuisine: American
Time: 25 minutes
Serves: 4
Diet tags: gluten-free, high-protein, keto, low-carb

## Ingredients
- 6 cups Romaine lettuce, chopped
- 2 cups cooked chicken breast, diced
- 6 slices bacon, cooked crisp and crumbled
- 3 hard-boiled eggs, peeled and sliced
- 1 avocado, diced
- 1 cup cherry tomatoes, halved
- 1/2 cup blue cheese crumbs
- 2 green onions, sliced

### Red Wine Vinaigrette
- 1/3 cup olive oil
- 3 tbsp red wine vinegar
- 1 tsp Dijon mustard
- 1 garlic clove, minced
- Salt and black pepper

## Instructions
1. Whisk olive oil, red wine vinegar, Dijon mustard, minced garlic, salt, and pepper in a small bowl to make dressing.
2. Arrange chopped Romaine lettuce at the bottom of a large platter.
3. Arrange ingredients in neat parallel rows on top of lettuce: diced chicken, crumbled bacon, hard-boiled eggs, diced avocado, halved tomatoes, and blue cheese crumbs.
4. Garnish with sliced green onions.
5. Drizzle red wine vinaigrette over salad right before serving.
"""
    },

    # ── CHINA (10) ──────────────────────────────────────────────────────────
    {
        "filename": "cn_kung_pao_chicken.md",
        "content": """# Authentic Sichuan Kung Pao Chicken

Cuisine: Chinese
Time: 25 minutes
Serves: 3
Diet tags: dairy-free, high-protein

## Ingredients
- 400g chicken thigh, cut into 1/2-inch cubes
- 1/2 cup roasted unsalted peanuts
- 6 dried red chilies, snipped into halves
- 1 tsp Sichuan peppercorns
- 3 garlic cloves, sliced
- 1 inch ginger, minced
- 3 green onions, chopped into 1-inch lengths
- 2 tbsp peanut oil

### Chicken Marinade
- 1 tbsp soy sauce
- 1 tbsp Shaoxing rice wine
- 1 tsp cornstarch

### Kung Pao Sauce
- 1.5 tbsp dark soy sauce
- 1 tbsp black vinegar (Chinkiang vinegar)
- 1 tbsp sugar
- 1 tsp sesame oil
- 1 tsp cornstarch mixed with 2 tbsp water

## Instructions
1. Marinate chicken cubes with soy sauce, Shaoxing wine, and cornstarch for 15 minutes.
2. Whisk dark soy sauce, black vinegar, sugar, sesame oil, cornstarch, and water to make Kung Pao sauce.
3. Heat peanut oil in a wok over high heat. Add marinated chicken and stir-fry for 3-4 minutes until cooked through. Remove chicken.
4. Add dried red chilies and Sichuan peppercorns to wok; stir-fry 30 seconds until fragrant.
5. Add garlic, ginger, and green onion whites. Stir-fry 1 minute.
6. Return chicken to wok, pour in Kung Pao sauce, and toss rapidly for 1 minute until sauce thickens and glazes chicken.
7. Stir in roasted peanuts and green onion greens. Serve hot with steamed rice.
"""
    },
    {
        "filename": "cn_mapo_tofu.md",
        "content": """# Sichuan Spicy Mapo Tofu

Cuisine: Chinese
Time: 25 minutes
Serves: 4
Diet tags: dairy-free, gluten-free, high-protein

## Ingredients
- 450g soft or medium-firm tofu, cut into 3/4-inch cubes
- 150g ground pork or beef
- 2 tbsp Sichuan Doubanjiang (spicy broad bean paste)
- 1 tbsp fermented black beans (douchi), rinsed
- 1 tsp ground Sichuan peppercorn
- 3 garlic cloves, minced
- 1 inch ginger, minced
- 2 green onions, finely sliced
- 1 cup chicken or vegetable broth
- 1 tbsp cornstarch mixed with 2 tbsp water
- 2 tbsp chili oil

## Instructions
1. Gently simmer tofu cubes in salted hot water for 2 minutes. Drain carefully.
2. Heat chili oil in a wok over medium heat. Add ground pork and cook until browned and crispy.
3. Add Doubanjiang bean paste, black beans, garlic, and ginger. Stir-fry 2 minutes until oil turns red and aromatic.
4. Pour in chicken broth and bring to a simmer.
5. Carefully add drained tofu cubes to gravy. Simmer gently for 5 minutes to absorb flavor.
6. Stir cornstarch slurry and drizzle into wok, tossing gently until sauce thickens to coat tofu.
7. Sprinkle ground Sichuan peppercorns and sliced green onions on top. Serve sizzling hot with rice.
"""
    },
    {
        "filename": "cn_sweet_and_sour_pork.md",
        "content": """# Cantonese Sweet and Sour Pork

Cuisine: Chinese
Time: 35 minutes
Serves: 4
Diet tags: dairy-free, high-protein

## Ingredients
- 400g pork tenderloin, cut into bite-sized cubes
- 1 egg, beaten
- 1/2 cup cornstarch
- 1 bell pepper, cut into chunks
- 1/2 onion, cut into chunks
- 1/2 cup pineapple chunks
- Oil for deep frying

### Pork Marinade
- 1 tbsp soy sauce
- 1 tsp Shaoxing wine
- 1/4 tsp white pepper

### Sweet & Sour Sauce
- 3 tbsp ketchup
- 2 tbsp rice vinegar
- 2 tbsp plum sauce or sugar
- 1 tbsp soy sauce
- 1/3 cup water
- 1 tsp cornstarch

## Instructions
1. Marinate pork cubes with soy sauce, Shaoxing wine, and white pepper for 15 minutes.
2. Dip pork cubes in beaten egg, then coat thoroughly in cornstarch.
3. Heat oil in a deep pan to 350°F (175°C). Deep fry pork pieces for 4 minutes until light golden. Drain.
4. Fry pork a second time for 2 minutes at higher heat (375°F) until super crispy. Drain.
5. Whisk ketchup, vinegar, plum sauce, soy sauce, water, and cornstarch.
6. In a skillet with 1 tbsp oil, stir-fry bell peppers, onions, and pineapple chunks for 2 minutes.
7. Pour in sweet & sour sauce and boil until thick. Toss crispy pork into sauce for 30 seconds and serve immediately.
"""
    },
    {
        "filename": "cn_chicken_chow_mein.md",
        "content": """# Classic Chicken Chow Mein

Cuisine: Chinese
Time: 20 minutes
Serves: 3
Diet tags: dairy-free, high-protein

## Ingredients
- 250g fresh egg noodles (chow mein noodles)
- 200g chicken breast, thinly sliced
- 1 cup cabbage, shredded
- 1 carrot, julienned
- 1 cup bean sprouts
- 3 green onions, cut into 2-inch lengths
- 2 garlic cloves, minced
- 2 tbsp vegetable oil

### Sauce
- 2 tbsp soy sauce
- 1 tbsp dark soy sauce
- 1 tbsp oyster sauce
- 1 tsp sesame oil
- 1/2 tsp sugar
- 1/4 tsp white pepper powder

## Instructions
1. Cook egg noodles in boiling water for 1-2 minutes until al dente. Drain and toss with 1 tsp oil.
2. Marinate sliced chicken with 1 tsp soy sauce and 1 tsp cornstarch for 10 minutes.
3. Whisk soy sauce, dark soy sauce, oyster sauce, sesame oil, sugar, and white pepper.
4. Heat 1 tbsp oil in a wok over high heat. Add sliced chicken and stir-fry 3 minutes until cooked. Set aside.
5. Heat remaining oil in wok. Add garlic, shredded cabbage, carrot, and green onions. Stir-fry 2 minutes.
6. Add cooked noodles, chicken, bean sprouts, and chow mein sauce.
7. Toss everything vigorously over high heat for 2 minutes until noodles are hot and coated. Serve warm.
"""
    },
    {
        "filename": "cn_pork_dumplings_jiaozi.md",
        "content": """# Steamed Chinese Pork Dumplings (Jiaozi)

Cuisine: Chinese
Time: 45 minutes
Serves: 4
Diet tags: dairy-free, high-protein

## Ingredients
- 30 round dumpling wrappers (store-bought or homemade)
- 300g ground pork
- 1 cup napa cabbage, finely chopped and squeezed of liquid
- 3 green onions, finely minced
- 1 tbsp ginger, finely grated
- 2 garlic cloves, minced
- 1.5 tbsp soy sauce
- 1 tbsp Shaoxing rice wine
- 1 tbsp sesame oil
- 1/2 tsp white pepper
- Salt to taste

### Dipping Sauce
- 2 tbsp soy sauce
- 1 tbsp Chinkiang black vinegar
- 1 tsp chili oil
- Shredded ginger

## Instructions
1. Combine ground pork, cabbage, green onions, ginger, garlic, soy sauce, Shaoxing wine, sesame oil, white pepper, and salt in a bowl. Mix vigorously in one direction until cohesive.
2. Place 1 tablespoon of pork filling in center of a dumpling wrapper.
3. Moisten wrapper edges with water. Fold in half and pleat top edge to seal securely.
4. Line bamboo steamer with parchment paper. Arrange dumplings without touching.
5. Steam over boiling water for 10-12 minutes until cooked through and wrapper turns translucent.
6. Mix dipping sauce ingredients and serve warm with steamed dumplings.
"""
    },
    {
        "filename": "cn_yangzhou_fried_rice.md",
        "content": """# Authentic Yangzhou Fried Rice

Cuisine: Chinese
Time: 20 minutes
Serves: 4
Diet tags: dairy-free, gluten-free, high-protein

## Ingredients
- 4 cups cold day-old cooked jasmine rice
- 2 eggs, beaten
- 1/2 cup cooked char siu (barbecue pork) or ham, diced
- 1/2 cup small shrimp, peeled and cooked
- 1/2 cup green peas
- 1/2 cup carrots, finely diced
- 3 green onions, sliced
- 3 tbsp vegetable oil
- 1 tbsp soy sauce
- 1/2 tsp sesame oil
- Salt and white pepper to taste

## Instructions
1. Heat 1 tbsp oil in a large wok over high heat. Add beaten eggs and scramble quickly until set. Remove egg.
2. Add remaining oil to wok. Add diced char siu pork, shrimp, peas, and carrots. Stir-fry 2 minutes.
3. Add cold cooked rice, breaking up any lumps with spatula. Stir-fry over high heat for 3-4 minutes until rice grains are hot and separated.
4. Return scrambled eggs to wok.
5. Season with soy sauce, sesame oil, salt, and white pepper.
6. Toss green onions into rice and stir-fry for another 30 seconds. Serve hot.
"""
    },
    {
        "filename": "cn_hainanese_chicken_rice.md",
        "content": """# Hainanese Chicken Rice

Cuisine: Chinese
Time: 50 minutes
Serves: 4
Diet tags: dairy-free, gluten-free, high-protein

## Ingredients
- 1 whole chicken (1.2kg)
- 4 slices ginger
- 2 stalks green onion
- 1 tbsp sesame oil
- Ice water bath

### Seasoned Rice
- 2 cups jasmine rice, washed and drained
- 2 tbsp chicken fat or oil
- 3 garlic cloves, minced
- 1 inch ginger, minced
- 2.5 cups reserved chicken poaching broth
- 1/2 tsp salt

### Chili Ginger Dip
- 4 red chilies
- 1 inch ginger
- 2 garlic cloves
- 1 tbsp lime juice
- 2 tbsp chicken broth

## Instructions
1. Stuff chicken cavity with ginger slices and green onions. Rub chicken skin with salt.
2. Bring a large pot of water to boil. Submerge chicken, lower heat to gentle simmer, cover, and cook 40 minutes.
3. Transfer chicken immediately into ice water bath for 10 minutes to crisp skin. Brush with sesame oil, carve into pieces.
4. For Rice: Heat chicken fat/oil in a pot. Sauté garlic and ginger until fragrant. Add rice and stir 2 minutes.
5. Add 2.5 cups hot chicken broth and salt. Bring to boil, cover, lower heat, and cook 15 minutes. Rest 10 minutes.
6. Blend chilies, ginger, garlic, lime juice, and chicken broth into a smooth sauce.
7. Serve carved poached chicken over seasoned rice alongside chili dip and warm chicken broth.
"""
    },
    {
        "filename": "cn_vegetable_spring_rolls.md",
        "content": """# Crispy Chinese Vegetable Spring Rolls

Cuisine: Chinese
Time: 35 minutes
Serves: 4
Diet tags: vegan, vegetarian, dairy-free

## Ingredients
- 12 spring roll wrappers (pastry sheets)
- 2 cups shredded cabbage
- 1 cup carrot, julienned
- 1 cup shiitake mushrooms, thinly sliced
- 1 cup bean sprouts
- 2 garlic cloves, minced
- 1 tbsp soy sauce
- 1 tbsp vegetarian oyster sauce
- 1 tsp sesame oil
- 1 tbsp cornstarch mixed with 2 tbsp water (sealing paste)
- Oil for deep frying

## Instructions
1. Heat 1 tbsp oil in a skillet. Add garlic, shiitake mushrooms, cabbage, and carrots. Stir-fry 3 minutes until tender.
2. Add bean sprouts, soy sauce, vegetarian oyster sauce, and sesame oil. Cook 1 minute. Cool filling completely.
3. Place a spring roll wrapper diamond-style. Spoon 2 tbsp filling on lower center.
4. Fold bottom corner up over filling, fold side corners inward, and roll tightly toward top. Seal top corner with cornstarch paste.
5. Heat oil to 350°F (175°C). Deep fry spring rolls in batches for 3-4 minutes until golden brown and crispy.
6. Drain on paper towels and serve with sweet chili sauce.
"""
    },
    {
        "filename": "cn_hot_and_sour_soup.md",
        "content": """# Classic Sichuan Hot and Sour Soup

Cuisine: Chinese
Time: 25 minutes
Serves: 4
Diet tags: dairy-free, high-protein, low-carb

## Ingredients
- 4 cups chicken or vegetable broth
- 150g firm tofu, sliced into matchsticks
- 5 wood ear mushrooms (soaked and sliced)
- 1/4 cup bamboo shoots, julienned
- 1 egg, beaten
- 2 tbsp soy sauce
- 1 tbsp dark soy sauce
- 3 tbsp Chinkiang black vinegar
- 1 tsp white pepper powder
- 2 tbsp cornstarch mixed with 3 tbsp water
- 1 tsp sesame oil
- 2 green onions, chopped

## Instructions
1. Bring chicken broth to a boil in a pot. Add wood ear mushrooms, bamboo shoots, and tofu matchsticks. Simmer 3 minutes.
2. Add soy sauce and dark soy sauce.
3. Stir cornstarch slurry and pour into boiling soup while stirring until broth thickens.
4. Turn off heat. Slowly drizzle beaten egg in a thin stream while gently swirling soup to create egg ribbons.
5. Stir in black vinegar, white pepper, and sesame oil (adding vinegar at the end preserves sharp tang).
6. Ladle into bowls and garnish with sliced green onions.
"""
    },
    {
        "filename": "cn_peking_style_chicken.md",
        "content": """# Crispy Peking Style Roasted Chicken

Cuisine: Chinese
Time: 60 minutes
Serves: 4
Diet tags: dairy-free, high-protein

## Ingredients
- 1kg chicken (whole or bone-in thighs)
- 2 tbsp hoisin sauce
- 1 tbsp soy sauce
- 1 tbsp honey or maltose
- 1 tbsp Five-Spice powder
- 1 tbsp Shaoxing wine
- 1 inch ginger, minced
- 2 garlic cloves, minced
- Cucumber matchsticks & green onion strips for serving
- Small Chinese Mandarin pancakes or tortillas

## Instructions
1. Mix hoisin sauce, soy sauce, honey, five-spice powder, Shaoxing wine, ginger, and garlic into a glaze marinade.
2. Rub chicken inside and out with marinade. Marinate in refrigerator for at least 2 hours (or overnight for crispy skin).
3. Preheat oven to 400°F (200°C). Place chicken on a rack over a roasting pan lined with water.
4. Roast for 45-50 minutes, basting twice with remaining glaze, until skin turns dark mahogany and crispy.
5. Rest chicken 10 minutes, then slice crispy meat.
6. Serve warm sliced chicken folded inside pancakes with hoisin sauce, cucumber, and green onion strips.
"""
    },

    # ── ENGLAND / BRITAIN (10) ──────────────────────────────────────────────
    {
        "filename": "uk_fish_and_chips.md",
        "content": """# British Beer-Battered Fish and Chips

Cuisine: British, English
Time: 35 minutes
Serves: 4
Diet tags: dairy-free, high-protein

## Ingredients
- 4 cod or haddock fillets (180g each)
- 1 cup all-purpose flour
- 1 tsp baking powder
- 1 cup ice-cold dark beer or ale
- 4 large Maris Piper potatoes, cut into thick chip batons
- Salt and malt vinegar
- Tartar sauce & lemon wedges
- Oil for deep frying

## Instructions
1. Parboil potato chips in salted boiling water for 5 minutes. Drain and dry thoroughly.
2. Fry chips in oil at 320°F (160°C) for 5 minutes (first blanching fry). Remove chips and drain.
3. Whisk flour, baking powder, salt, and cold beer together into a smooth batter.
4. Dust fish fillets lightly with flour, then dip into cold beer batter to coat completely.
5. Deep fry battered fish in hot oil at 375°F (190°C) for 5-6 minutes until batter is golden and crispy.
6. Increase oil heat to 380°F and fry chips a second time for 3 minutes until crisp and golden.
7. Season hot fish and chips generously with sea salt and malt vinegar. Serve immediately with tartar sauce.
"""
    },
    {
        "filename": "uk_shepherds_pie.md",
        "content": """# Traditional British Shepherd's Pie

Cuisine: British, English
Time: 60 minutes
Serves: 6
Diet tags: gluten-free, high-protein

## Ingredients
- 700g ground lamb (minced lamb)
- 1 tbsp olive oil
- 1 large onion, diced
- 2 carrots, diced
- 2 celery stalks, diced
- 2 garlic cloves, minced
- 2 tbsp tomato paste
- 2 tbsp Worcestershire sauce
- 1 cup beef or lamb broth
- 1 cup frozen green peas
- 1 tsp dried thyme & rosemary

### Mashed Potato Topping
- 1kg potatoes, peeled and cut
- 4 tbsp butter
- 1/3 cup milk or cream
- 1/2 cup cheddar cheese, grated
- Salt, pepper, and nutmeg

## Instructions
1. Boil potatoes in salted water for 15 minutes until soft. Drain and mash with butter, milk, salt, pepper, and nutmeg.
2. Heat oil in a skillet. Add minced lamb and brown for 6 minutes. Drain excess fat.
3. Add onion, carrots, celery, and garlic. Cook 5 minutes until soft.
4. Stir in tomato paste, Worcestershire sauce, thyme, rosemary, salt, pepper, and broth. Simmer 15 minutes until gravy thickens.
5. Stir green peas into meat mixture. Transfer to a 9x13 baking dish.
6. Spread mashed potatoes evenly over lamb filling. Drag tines of a fork across top to create ridges. Sprinkle cheddar cheese.
7. Bake at 400°F (200°C) for 25-30 minutes until potato top turns crisp and golden.
"""
    },
    {
        "filename": "uk_beef_wellington.md",
        "content": """# Classic British Beef Wellington

Cuisine: British, English
Time: 90 minutes
Serves: 6
Diet tags: high-protein

## Ingredients
- 800g beef center-cut fillet (tenderloin)
- 2 tbsp olive oil
- 2 tbsp English mustard
- 400g mushrooms (cremini/button), finely chopped (duxelles)
- 2 tbsp butter
- 8 slices Prosciutto or Parma ham
- 1 sheet puff pastry (thawed)
- 2 egg yolks, beaten for egg wash
- Coarse sea salt

## Instructions
1. Season beef fillet with salt and pepper. Sear quickly in hot oil on all sides for 2 minutes total. Brush all over with English mustard while warm. Cool completely.
2. Sauté chopped mushrooms in butter over medium-high heat for 10-12 minutes until all moisture evaporates completely. Cool.
3. Lay a sheet of plastic wrap on counter. Arrange prosciutto slices in overlapping layer. Spread mushroom duxelles over prosciutto.
4. Place seared beef fillet in center. Wrap tightly into a log using plastic wrap. Chill 20 minutes.
5. Roll out puff pastry sheet. Unwrap beef log and place onto pastry. Roll pastry around beef, sealing seams with egg wash.
6. Wrap tightly in plastic and chill 15 minutes.
7. Preheat oven to 400°F (200°C). Place Wellington on parchment-lined baking sheet, brush with egg wash, score lattice pattern.
8. Bake 30-35 minutes until pastry is golden and meat thermometer reads 125°F (medium-rare). Rest 10 minutes before carving.
"""
    },
    {
        "filename": "uk_full_english_breakfast.md",
        "content": """# Traditional Full English Breakfast

Cuisine: British, English
Time: 25 minutes
Serves: 2
Diet tags: high-protein

## Ingredients
- 4 British pork sausages (cumberlands)
- 4 slices back bacon
- 2 thick slices black pudding
- 2 eggs
- 1 cup canned baked beans in tomato sauce
- 1 cup button mushrooms, halved
- 1 large tomato, halved
- 2 slices white bread
- Butter for frying
- Salt and black pepper

## Instructions
1. Heat oven to warm (200°F) to hold cooked items.
2. In a large skillet over medium heat, cook pork sausages for 10-12 minutes until cooked through. Transfer to warm plate.
3. In same skillet, cook back bacon for 4 minutes and black pudding slices for 3 minutes per side.
4. Warm baked beans in a small saucepan.
5. Fry tomato halves cut-side down and button mushrooms in bacon fat for 4 minutes until golden.
6. Melt butter in skillet and fry bread slices until golden brown and crispy.
7. Fry eggs sunny-side up in melted butter until whites are set and yolks are runny.
8. Plate sausages, bacon, black pudding, eggs, baked beans, tomatoes, mushrooms, and fried bread together with hot English tea.
"""
    },
    {
        "filename": "uk_sunday_roast_beef.md",
        "content": """# Sunday Roast Beef with Yorkshire Pudding

Cuisine: British, English
Time: 90 minutes
Serves: 6
Diet tags: high-protein

## Ingredients
- 1.5kg beef rib roast or topside joint
- 2 tbsp olive oil
- 1 tbsp fresh rosemary, chopped
- 1 tbsp fresh thyme, chopped
- Salt and black pepper

### Yorkshire Pudding Batter
- 1 cup all-purpose flour
- 1 cup milk
- 4 eggs
- Beef drippings or oil for tins

### Onion Gravy
- Pan drippings
- 1 onion, sliced
- 2 tbsp flour
- 2 cups beef stock

## Instructions
1. Rub beef roast with olive oil, rosemary, thyme, salt, and pepper.
2. Roast at 425°F (220°C) for 20 minutes, then lower heat to 350°F (175°C) and roast 40 minutes for medium-rare (internal temp 135°F). Transfer beef to board, cover, and rest 20 minutes.
3. Whisk flour, milk, eggs, and salt into smooth Yorkshire pudding batter. Rest 30 minutes.
4. Put 1 tsp beef drippings into each hole of a 12-cup muffin tin. Heat tin in 425°F oven for 10 minutes until smoking hot.
5. Pour batter into hot muffin tin holes. Bake 20-22 minutes without opening oven door until puffed high and golden.
6. Make Gravy: Sauté sliced onion in roasting pan drippings. Whisk in flour, then pour beef stock and simmer until rich and thick.
7. Slice roast beef thinly and serve with warm Yorkshire puddings, roast potatoes, and hot onion gravy.
"""
    },
    {
        "filename": "uk_chicken_tikka_masala.md",
        "content": """# Classic British Chicken Tikka Masala

Cuisine: British, English
Time: 45 minutes
Serves: 4
Diet tags: gluten-free, high-protein

## Ingredients
- 600g boneless chicken thighs, cut into cubes
- 1/2 cup plain yogurt
- 1 tbsp lemon juice
- 1 tbsp garam masala
- 1 tsp cumin powder
- 1 tsp turmeric
- 1 tbsp ginger-garlic paste

### Masala Sauce
- 2 tbsp butter
- 1 tbsp oil
- 1 large onion, finely chopped
- 4 garlic cloves, minced
- 1 inch ginger, grated
- 1 tbsp garam masala
- 1 tsp coriander powder
- 1 tsp paprika
- 1 can (14 oz) tomato sauce or passata
- 1/2 cup heavy cream
- Salt to taste

## Instructions
1. Marinate chicken with yogurt, lemon juice, ginger-garlic paste, garam masala, cumin, and turmeric for 30 minutes.
2. Thread chicken on skewers and broil under high oven broiler for 10-12 minutes until charred at edges.
3. Heat butter and oil in a large skillet. Add chopped onion, garlic, and ginger. Sauté 6 minutes until soft.
4. Stir in garam masala, coriander powder, paprika, and salt. Cook 1 minute.
5. Pour in tomato passata and simmer 15 minutes until sauce thickens.
6. Stir in heavy cream and broiled chicken pieces. Simmer gently for 8 minutes.
7. Garnish with fresh coriander and serve hot with pilau rice and garlic naan.
"""
    },
    {
        "filename": "uk_toad_in_the_hole.md",
        "content": """# British Toad in the Hole

Cuisine: British, English
Time: 45 minutes
Serves: 4
Diet tags: high-protein

## Ingredients
- 8 high-quality British pork sausages
- 2 tbsp vegetable oil or lard

### Yorkshire Batter
- 1 cup all-purpose flour
- 3 eggs
- 1 cup milk
- 1 tsp Dijon mustard
- 1 pinch salt and pepper

### Rich Onion Gravy
- 2 large onions, thinly sliced
- 2 tbsp butter
- 1 tbsp flour
- 2 cups beef stock
- 1 tsp Worcestershire sauce

## Instructions
1. Whisk flour, eggs, milk, Dijon mustard, salt, and pepper until smooth. Rest batter for 20 minutes.
2. Preheat oven to 425°F (220°C).
3. Put oil and sausages into a large metal baking dish (9x13 inch). Bake for 10 minutes until sausages sizzle and brown slightly.
4. Carefully remove baking dish from oven. Immediately pour Yorkshire batter around hot sizzling sausages.
5. Return to oven immediately and bake for 25-30 minutes without opening oven door, until batter rises high, crisp, and golden brown.
6. Meanwhile, caramelize sliced onions in butter. Whisk in flour, then beef stock and Worcestershire sauce. Simmer 10 minutes into thick gravy.
7. Serve hot slices of Toad in the Hole drenched in warm onion gravy.
"""
    },
    {
        "filename": "uk_bangers_and_mash.md",
        "content": """# Classic Bangers and Mash with Onion Gravy

Cuisine: British, English
Time: 35 minutes
Serves: 4
Diet tags: gluten-free, high-protein

## Ingredients
- 8 thick pork sausages (bangers)
- 1 tbsp oil

### Creamy Mash
- 1kg Yukon Gold potatoes, peeled and cubed
- 4 tbsp butter
- 1/3 cup warm milk or cream
- Salt and black pepper

### Onion Gravy
- 2 large brown onions, sliced into half-moons
- 2 tbsp butter
- 1 tbsp flour
- 2 cups beef broth
- 1 tbsp Worcestershire sauce
- 1 tsp Dijon mustard

## Instructions
1. Boil potatoes in salted water for 15 minutes until tender. Drain well, mash thoroughly with butter, warm milk, salt, and pepper until velvety smooth.
2. Heat oil in a large skillet over medium heat. Fry pork sausages for 12-15 minutes, turning regularly until golden brown and cooked through. Remove sausages.
3. In the same skillet, melt 2 tbsp butter. Add sliced onions and cook over medium-low heat for 12 minutes until dark caramelized brown.
4. Sprinkle flour over onions and cook 1 minute.
5. Slowly pour in beef broth while stirring. Add Worcestershire sauce and Dijon mustard. Simmer 8 minutes until gravy thickens.
6. Mound creamy mashed potatoes onto plates, lay warm sausages on top, and pour generous amounts of rich onion gravy over everything.
"""
    },
    {
        "filename": "uk_victoria_sponge.md",
        "content": """# Traditional Victoria Sponge Cake

Cuisine: British, English
Time: 40 minutes
Serves: 8
Diet tags: vegetarian

## Ingredients
- 200g unsalted butter, softened
- 200g caster sugar (superfine sugar)
- 4 large eggs, room temperature
- 200g self-raising flour, sifted
- 1 tsp vanilla extract
- 1 tbsp milk

### Filling & Topping
- 1/2 cup strawberry or raspberry jam
- 1/2 cup heavy double cream, whipped to soft peaks
- Dusting of powdered icing sugar

## Instructions
1. Preheat oven to 350°F (180°C). Grease two 8-inch round cake tins and line bases with parchment paper.
2. Cream softened butter and caster sugar together in a large bowl with electric mixer for 4 minutes until light and fluffy.
3. Add eggs one at a time, beating well after each addition. Mix in vanilla extract.
4. Gently fold in sifted self-raising flour and milk using a metal spoon until smooth.
5. Divide batter evenly between the two prepared cake tins. Smooth tops.
6. Bake for 20-22 minutes until golden brown and a skewer inserted comes out clean. Cool completely on wire racks.
7. Spread strawberry jam on bottom layer, top with whipped double cream, and place second cake layer on top.
8. Dust top generously with powdered icing sugar before serving with afternoon tea.
"""
    },
    {
        "filename": "uk_cornish_pasties.md",
        "content": """# Traditional Cornish Pasties

Cuisine: British, English
Time: 60 minutes
Serves: 4
Diet tags: high-protein

## Ingredients
- 400g shortcrust pastry (store-bought or homemade)
- 300g beef skirt steak or sirloin, finely diced
- 150g swede (rutabaga) or turnip, finely diced
- 150g potatoes, finely diced
- 1 large onion, finely chopped
- Salt and coarsely ground black pepper
- 2 tbsp butter
- 1 egg beaten with 1 tbsp water for egg wash

## Instructions
1. Preheat oven to 400°F (200°C). Line a baking sheet with parchment paper.
2. Mix diced raw beef steak, swede, potatoes, and onion together in a bowl. Season generously with sea salt and black pepper.
3. Roll out shortcrust pastry and cut out four 8-inch circles.
4. Divide beef and vegetable filling evenly onto center of each pastry circle. Dot 1/2 tbsp butter on top of filling.
5. Brush edges of pastry with water. Fold pastry over filling to form a half-moon shape.
6. Crimp edges tightly together using fingers to form a traditional rope seam along the side.
7. Place pasties on baking sheet. Brush tops with egg wash and cut a small steam vent slit on top.
8. Bake at 400°F for 20 minutes, then lower heat to 350°F (175°C) and bake another 25 minutes until golden brown. Cool 10 minutes before eating.
"""
    }
]

def main():
    os.makedirs(TEXT_DIR, exist_ok=True)
    created_count = 0
    for r in recipes:
        filepath = os.path.join(TEXT_DIR, r["filename"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(r["content"].strip() + "\n")
        created_count += 1
        print(f"Created recipe: {r['filename']}")
    print(f"\nSuccessfully created {created_count} new recipes in {TEXT_DIR}!")

if __name__ == "__main__":
    main()
