from SkinCareApp.models import SkinType, SkincareProduct, SkincareRoutine, RoutineSkinType, AboutSkinTypes

SkinType.objects.create(
    name='Dry Skin',
    description='Dry skin lacks moisture and may feel tight or itchy. It may also appear flaky or rough.'
)

SkinType.objects.create(
    name='Oily Skin',
    description='Oily skin is characterized by excess sebum production, often leading to a shiny complexion and enlarged pores.'
)

SkinType.objects.create(
    name='Combination Skin',
    description='Combination skin has both oily and dry areas. Typically, the T-zone (forehead, nose, and chin) is oily, while the cheeks are dry or normal.'
)

SkinType.objects.create(
    name='Sensitive Skin',
    description='Sensitive skin is easily irritated by various factors such as skincare products, weather, or environmental factors. It may react with redness, itching, or burning sensations.'
)

SkinType.objects.create(
    name='Normal Skin',
    description='Normal skin is well-balanced, neither too oily nor too dry. It has minimal imperfections, fine pores, and a radiant complexion.'
)


def create_skincare_routine(name: str, description: str) -> SkincareRoutine:
    """
    Creates a new skincare routine.

    Parameters:
        name (str): The name of the skincare routine.
        description (str): The description of the skincare routine.

    Returns:
        SkincareRoutine: The newly created skincare routine object.
    """
    return SkincareRoutine.objects.create(name=name, description=description)

def create_skincare_product(name: str, description_product: str, image_url: str, product_url: str, routine: SkincareRoutine) -> SkincareProduct:
    """
    Creates a new skincare product associated with a skincare routine.

    Parameters:
        name (str): The name of the skincare product.
        description_product (str): The description of the skincare product.
        image_url (str): The URL of the image representing the skincare product.
        product_url (str): The URL of the product page for the skincare product.
        routine (SkincareRoutine): The skincare routine associated with the product.

    Returns:
        SkincareProduct: The newly created skincare product object.
    """
    return SkincareProduct.objects.create(
        name=name,
        description_product=description_product,
        image_url=image_url,
        product_url=product_url,
        routine=routine
)


# All Skincare Routines
cleansing_dry = create_skincare_routine(
    name='Gentle Cleansing',
    description='Use a mild cleanser or cleansing lotion that is soap-free and alcohol-free. Avoid using hot water, as it can further dry out your skin.'
)

create_skincare_product(
    name='Micellar Water',
    description_product="Bioderma Micellar Water is a gentle cleansing water that removes makeup and impurities without rinsing. To use, apply it to a cotton pad and gently wipe over your face and eyes. No rinsing required. Suitable for all skin types, including sensitive skin.",
    image_url='https://www.helpnet.ro/data/images/img-large-product/4/3_25794.jpg?_gl=1*1fqf2in*_up*MQ..&gclid=CjwKCAjwl4yyBhAgEiwADSEjeAzvjErJai4i4ae4pfVQngQvMyBCGfTIuck5zoLMJSAmEacpPt0U8BoCgUYQAvD_BwE',
    product_url='https://www.helpnet.ro/bioderma-sensibio-h2o-lotiune-micelara-500ml?gclid=CjwKCAjwl4yyBhAgEiwADSEjeAzvjErJai4i4ae4pfVQngQvMyBCGfTIuck5zoLMJSAmEacpPt0U8BoCgUYQAvD_BwE',
    routine=cleansing_dry
)

create_skincare_product(
    name='Cleansing Milk',
    description_product="La Roche-Posay's cleansing milk effectively removes impurities and makeup while keeping sensitive skin balanced. To use, apply a small amount to damp skin, massage gently, and rinse thoroughly. Use morning and night for best results.",
    image_url='https://www.helpnet.ro/data/images/img-large-product/2/3_30602.jpg',
    product_url='https://www.helpnet.ro/la-roche-posay-toleriane-lapte-demachiant-pentru-toate-tipurile-de-ten-intolerant-200ml?gclid=CjwKCAjwl4yyBhAgEiwADSEjeKMDwzbyv0ulWLR5C5ByAmzcSi8UyU-ogKOGKVFtssAMZlIfRNQvrBoCyfAQAvD_BwE',
    routine=cleansing_dry
)

exfoliation_dry = create_skincare_routine(
    name='Gentle Exfoliation',
    description="'Regular exfoliation helps remove dead skin cells from the surface, but for dry skin, it's important to use a gentle exfoliant once or twice a week to avoid irritating sensitive skin."
)

SkincareProduct.objects.create(
    name='Face Scrub',
    description_product="The face scrub serves to exfoliate the skin, removing dead cells and impurities, resulting in a smoother complexion. To use, apply a small amount to damp skin, massage gently in circular motions, and then rinse thoroughly. It's recommended to use the scrub 2-3 times a week for optimal results.",
    image_url='https://cdn.greek-shop.ro/media/catalog/product/cache/1/image/af097278c5db4767b0fe9bb92fe21690/_/l/_liv_classic_face_scrub_150ml.jpg',
    product_url="https://www.greek-shop.ro/olivolio-scrub-fata-natural-cu-ulei-de-masline.html?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjePA5OXbdn3srd7vfRycWWOtq-h4dJ2wnKlFsItouJKz5bAZ4n7DRTBoCHzwQAvD_BwE",
    routine=exfoliation_dry
)

hydration_dry = create_skincare_routine(
    name='Intense Hydration',
    description="Choose a rich moisturizer with emollient and humectant ingredients such as hyaluronic acid, glycerin, natural butters (shea butter, cocoa butter), or vegetable oils (sweet almond oil, jojoba oil). Apply it twice a day, morning and evening, after cleansing."
)

SkincareProduct.objects.create(
    name='Hydrating Cream',
    description_product = "Nuoderm face cream is designed to moisturize and nourish the skin, helping to improve its texture and appearance. To use, apply a small amount to clean, dry skin, and gently massage in circular motions until fully absorbed. Use morning and night for best results.",
    image_url='https://nuoderm.ro/cdn/shop/products/Snail_1800x1800.jpg?v=1662495410',
    product_url="https://nuoderm.ro/products/crema-melc?variant=40789913632819&currency=RON&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjePWhN9zhcaas-pRtnXbOpeVIHLa7xu74o4t82LG2lSWEz62Fh4SoyxoCZz8QAvD_BwE",
    routine=hydration_dry
)

SkincareProduct.objects.create(
    name='Hydrating Serum',
    description_product="The Hydrating Hydro Boost Serum is formulated to deeply moisturize the skin, providing intense hydration and helping to plump and smooth the complexion. To use, apply a few drops to clean, dry skin, gently patting it onto the face and neck until fully absorbed. Follow with your favorite moisturizer. For optimal results, use daily, morning and night.",
    image_url='https://bewellstore.ro/wp-content/uploads/2023/11/HYDRO-BOOST-Product.jpg',
    product_url="https://bewellstore.ro/product/intensive-hydrating-serum-hydro-boost-30ml-numee/?utm_source=Google+Shopping&utm_medium=cpc&utm_campaign=google-shopping&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeKYdbnDToBiWUInpo6GwyHq3H-3stig-UrpWt3MFy9PWhDlanP0r4BoCAPUQAvD_BwE",
    routine=hydration_dry
)

SkincareProduct.objects.create(
    name='Hialuronic Acid',
    description_product="The Hyaluronic Acid Serum serves to hydrate and plump the skin, reducing the appearance of fine lines and wrinkles. To use, apply a small amount to cleansed skin, gently massaging it in until fully absorbed. Follow with your moisturizer. For best results, use daily, morning and night",
    image_url='https://static.sole.ro/cs-photos/products/original/queen-of-hydration-1-hyaluronic-acid-panthenol-ser-de-fata-30-ml_25663_3_1695296685.jpg',
    product_url="https://www.sole.ro/ingrijire-personala/ten/elyn-s-lab-queen-of-hydration-1-hyaluronic-acid-panthenol-ser-de-fata-30-ml-f78418?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeJIjAZN2IbsdgpRZ8gp1aIGCDZrANMbjTQVef8TotxTMMI1tU-1FdRoCkHYQAvD_BwE",
    routine=hydration_dry
)

SkincareProduct.objects.create(
    name='Hydrating Mask',
    description_product="The Galenic Hydrating Mask aims to deeply moisturize the skin, providing intense hydration and leaving it feeling soft and supple.For best results, use 1-2 times per week.",
    image_url='https://cdn.contentspeed.ro/magnapharm.websales.ro/cs-content/cs-photos/products/original/galnic-masc-hidratant-50-ml_8398_1_16487251278913.png',
    product_url="https://www.magnabeauty.ro/masti-si-patch-uri/galenic-masca-hidratanta-50-ml-33642.html?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeMRhs8_RtIE0HnB_G_po8yPlbijdCqThBFSMXuKtaAw2on7ppZ3yuBoCxh4QAvD_BwE",
    routine=hydration_dry
)


sun_protection = create_skincare_routine(
    name='Sun Protection',
    description="Don't forget to use a sunscreen with a high protection factor (SPF 30 or higher) every day, even on cloudy days or during winter. This will protect you from the harmful effects of UV rays and prevent premature aging and drying of the skin."
)

SkincareProduct.objects.create(
    name='Sun Protection Spray',
    description_product="The La Roche-Posay sunscreen spray offers broad-spectrum protection against harmful UV rays, helping to prevent sunburn and premature skin aging. To use, shake the bottle well, then spray evenly onto exposed skin 15 minutes before sun exposure. Reapply every 2 hours or after swimming or sweating. Avoid spraying directly onto the face; instead, spray onto hands and then apply to the face",
    image_url='https://www.helpnet.ro/data/images/img-large-product/0/3_35480.jpg',
    product_url="https://www.helpnet.ro/la-roche-posay-anthelios-spray-invizibil-spf50-x-75ml?gclid=CjwKCAjwl4yyBhAgEiwADSEjeGG55PzhdjT2PiZ413ioi4T8UBC2RoL_E0bSj_UpgcO8KHala--HKxoCiQ4QAvD_BwE",
    routine=sun_protection
)

SkincareProduct.objects.create(
    name='Sun Protection Cream',
    description_product="The Nuoderm SPF 50 sunscreen cream provides high-level protection against harmful UV rays, helping to prevent sunburn and skin damage. To use, apply a generous amount to clean, dry skin at least 15 minutes before sun exposure. Reapply every 2 hours or after swimming or sweating. Avoid contact with eyes. For best results, use daily, especially when spending time outdoors.",
    image_url='https://neoderm.ro/wp-content/uploads/2023/09/Neoderm-Crema-SPF.png',
    product_url="https://neoderm.ro/product/crema-spf-50/?utm_source=Google%20Shopping&utm_campaign=Neoderm&utm_medium=cpc&utm_term=4538&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeIFnpanTGeWCs40erQJj002tIZVOplAenn_VIiIXzaxZozVKzbuRFxoCqv8QAvD_BwE#&gid=1&pid=1",
    routine=sun_protection
)

SkincareProduct.objects.create(
    name='Sun Protection Cream',
    description_product="The Uriage Hyseac SPF 50 sunscreen cream is designed to provide effective protection against harmful UV rays while controlling excess oil and shine. To use, apply a sufficient amount to clean, dry skin before sun exposure. Reapply every 2 hours or after swimming or sweating. Avoid contact with eyes. For optimal protection, use daily, particularly when spending prolonged periods outdoors",
    image_url='https://s13emagst.akamaized.net/products/33595/33594949/images/res_628f5d29a521e75e74b7184171924ba9.jpg?width=720&height=720&hash=EEA10F0D58ACA3E95D361AAFB67E7A8E',
    product_url="https://www.emag.ro/fluid-hidratant-uriage-hyseac-spf-50-50-ml-3661434001932/pd/DM0LH7MBM/?cmpid=86991&utm_source=google&utm_medium=cpc&utm_campaign=(RO:Whoop!)_1P_%3e_Cosmetice_and_Produse_ingrijire_personala&utm_content=82270135608&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeGT1SCW1BMHRuqHlDZrsepHeldcnOiKofdex9sc2ZFpqYProYIxrAxoCnCsQAvD_BwE",
    routine=sun_protection
)


drying_factors = create_skincare_routine(
    name='Avoiding Drying Factors',
    description="Try to avoid prolonged exposure to dry air or excessive heat, as these factors can worsen skin dryness. Also, be mindful of skincare products containing alcohol or irritating ingredients that can further dry out your skin."
)

aqua_consume = create_skincare_routine(
    name='Hydration from Within',
    description="Don't forget to drink enough water throughout the day to keep your skin hydrated from the inside out. A balanced diet rich in fruits and vegetables can also contribute to the health of your skin."
)

no_exfoliation = create_skincare_routine(
    name='Do not exfoliate the skin.',
    description="Exfoliation involves removing dead skin cells from the surface of the skin, which can be too harsh for sensitive skin. It may cause irritation, redness, or exacerbate existing skin conditions in individuals with sensitive skin. Therefore, it's best to avoid exfoliation in order to prevent potential adverse reactions"
)

cleansing_normal =create_skincare_routine(
    name='Normal Cleansing',
    description="In a basic skin care routine, cleansing is key. Start with a gentle cleanser, massage onto damp skin, rinse, and pat dry. Follow with your favorite products for a refreshed, healthy glow."
)

SkincareProduct.objects.create(
    name='Micellar Water',
    description_product= "Micellar water is a very gentle way to remove excess sebum, impurities, and makeup. CeraVe Micellar Water contains 3 essential ceramides and niacinamide and is based on a mild and easy-to-use formula that does not require rinsing.",
    image_url='https://www.cerave.ro/-/media/project/loreal/brand-sites/cerave/emea/ro/scx/products/pdp-packshot/miscellar-water/miscellar-water-front-lg.jpg?rev=bfb696896a434da0b2c9aa1fecbe5359?w=500&hash=C88949293DE678C10CC65BAD67DDBAE0',
    product_url='https://www.cerave.ro/toate-produsele/geluri-de-curatare-pentru-fata/apa-micelara-hidratanta?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeNoZLe4JZCEKXcqTytjQm_pU42HbQ247TTNa-tXLC1xgwnIbNbgzTRoCD3YQAvD_BwE&gclsrc=aw.ds',
    routine=cleansing_normal
)


hydration_normal = create_skincare_routine(
    name='Normal Hydration',
    description="For normal skin hydration, use a light moisturizer. Apply a small amount evenly, focusing on dry areas, for soft, balanced skin."
)

SkincareProduct.objects.create(
    name='Hydrating Cream',
    description_product = "Nuoderm face cream is designed to moisturize and nourish the skin, helping to improve its texture and appearance. To use, apply a small amount to clean, dry skin, and gently massage in circular motions until fully absorbed. Use morning and night for best results.",
    image_url='https://nuoderm.ro/cdn/shop/products/Snail_1800x1800.jpg?v=1662495410',
    product_url="https://nuoderm.ro/products/crema-melc?variant=40789913632819&currency=RON&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjePWhN9zhcaas-pRtnXbOpeVIHLa7xu74o4t82LG2lSWEz62Fh4SoyxoCZz8QAvD_BwE",
    routine=hydration_normal
)

SkincareProduct.objects.create(
    name='Hydrating Serum',
    description_product="The Hydrating Hydro Boost Serum is formulated to deeply moisturize the skin, providing intense hydration and helping to plump and smooth the complexion. To use, apply a few drops to clean, dry skin, gently patting it onto the face and neck until fully absorbed. Follow with your favorite moisturizer. For optimal results, use daily, morning and night.",
    image_url='https://bewellstore.ro/wp-content/uploads/2023/11/HYDRO-BOOST-Product.jpg',
    product_url="https://bewellstore.ro/product/intensive-hydrating-serum-hydro-boost-30ml-numee/?utm_source=Google+Shopping&utm_medium=cpc&utm_campaign=google-shopping&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeKYdbnDToBiWUInpo6GwyHq3H-3stig-UrpWt3MFy9PWhDlanP0r4BoCAPUQAvD_BwE",
    routine=hydration_normal
)

SkincareProduct.objects.create(
    name='Hialuronic Acid',
    description_product="The Hyaluronic Acid Serum serves to hydrate and plump the skin, reducing the appearance of fine lines and wrinkles. To use, apply a small amount to cleansed skin, gently massaging it in until fully absorbed. Follow with your moisturizer. For best results, use daily, morning and night",
    image_url='https://static.sole.ro/cs-photos/products/original/queen-of-hydration-1-hyaluronic-acid-panthenol-ser-de-fata-30-ml_25663_3_1695296685.jpg',
    product_url="https://www.sole.ro/ingrijire-personala/ten/elyn-s-lab-queen-of-hydration-1-hyaluronic-acid-panthenol-ser-de-fata-30-ml-f78418?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeJIjAZN2IbsdgpRZ8gp1aIGCDZrANMbjTQVef8TotxTMMI1tU-1FdRoCkHYQAvD_BwE",
    routine=hydration_normal
)

hydration_comb = create_skincare_routine(
    name='Light Hydration',
    description="For light hydration on slightly oily skin, choose a non-greasy moisturizer. Apply sparingly for a balanced, refreshed complexion."
)

SkincareProduct.objects.create(
    name='Hydrating Serum',
    description_product="The Hydrating Hydro Boost Serum is formulated to deeply moisturize the skin, providing intense hydration and helping to plump and smooth the complexion. To use, apply a few drops to clean, dry skin, gently patting it onto the face and neck until fully absorbed. Follow with your favorite moisturizer. For optimal results, use daily, morning and night.",
    image_url='https://bewellstore.ro/wp-content/uploads/2023/11/HYDRO-BOOST-Product.jpg',
    product_url="https://bewellstore.ro/product/intensive-hydrating-serum-hydro-boost-30ml-numee/?utm_source=Google+Shopping&utm_medium=cpc&utm_campaign=google-shopping&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeKYdbnDToBiWUInpo6GwyHq3H-3stig-UrpWt3MFy9PWhDlanP0r4BoCAPUQAvD_BwE",
    routine=hydration_comb
)

cleansing_oily = create_skincare_routine(
    name='Powerful Cleansing',
    description="For strong cleansing on oily skin, opt for a powerful cleanser. Apply to damp skin, massage thoroughly, then rinse for a refreshed, clarified complexion."
)

SkincareProduct.objects.create(
    name='Micellar Water For Acne and Oily Skin',
    description_product= "Micellar water is a very gentle way to remove excess sebum, impurities, and makeup. CeraVe Micellar Water contains 3 essential ceramides and niacinamide and is based on a mild and easy-to-use formula that does not require rinsing.",
    image_url='https://www.drmax.ro/_i/1253541768.webp?m2=%2Fmedia%2Fcatalog%2Fproduct%2Fa%2Fv%2Favene_apa_micelara.jpg&fit=contain&w=350&h=350&format=webp',
    product_url='https://www.drmax.ro/apa-micelara-pentru-ten-gras-cu-tendinta-acneica-cleanance-400-ml-avene?gclid=CjwKCAjwl4yyBhAgEiwADSEjeH9giqSBYO3XXbt2Hc9UcJLlAr12kqPjFZpZRSOOV4ylfzILztFUEBoCuOsQAvD_BwE',
    routine=cleansing_oily
)


stop_acne = create_skincare_routine(
    name='Fights Acne',
    description="For combating acne, try a targeted treatment. Apply directly to affected areas to reduce inflammation and breakouts, promoting clearer skin."
)

SkincareProduct.objects.create(
    name='Antiacne Cream',
    description_product="Anti-acne creams are skincare products designed to reduce acne breakouts. They contain ingredients like salicylic acid or benzoyl peroxide to unclog pores and reduce inflammation, promoting clearer skin.",
    image_url='https://cdn.notinoimg.com/detail_main_mq/avene/3282770144970_01-o/avene-cleanance-comedomed-ingrijire-intensiva-pentru-tratament-local___211201.jpg',
    product_url="https://www.notino.ro/avene/cleanance-comedomed-emulsie-faciala-pentru-tratament-local/p-16104152/?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeP5LeU7Cg10K9Vzlmmh5b6qV43VqZaCP12FdWzQfnzbTXFPATfocWRoCKLEQAvD_BwE",
    routine=stop_acne
)

SkincareProduct.objects.create(
    name='Antiacne Mask',
    description_product="Anti-acne masks are skincare treatments specifically formulated to target acne-prone skin. These masks often contain ingredients such as clay, sulfur, or charcoal, known for their ability to absorb excess oil and impurities from the skin. They help to unclog pores, reduce inflammation, and prevent future breakouts. Anti-acne masks can be used as part of a regular skincare routine to promote clearer, healthier-looking skin",
    image_url='https://www.kiehls.ro/dw/image/v2/AAQP_PRD/on/demandware.static/-/Sites-kie-master-catalog/default/dw70926c15/packshots-2021/Kiehls-face-mask-rare-earth-deep-pore-cleansing-masque-28ml-000-3605971023613-whip.jpg?sw=698&sh=698&sm=cut&sfrm=png&q=70',
    product_url="https://www.kiehls.ro/rare-earth-deep-pore-cleansing-mask---masca-pentru-curatarea-fetei-cu-argila-alba/792.html?dwvar_792_size=28%20ml&gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeKUiYi9T6R8BoAhiJ7STpFSQrqMy-9Pc9JHUDNAYyBLaxYnttM1QMxoCyNQQAvD_BwE",
    routine=stop_acne
)

specialist_consultation = create_skincare_routine(
    name='Specialist Consultation',
    description="We recommend presenting to a dermatologist for comprehensive analysis. The causes of acne are multiple, and treatments can have numerous local and systemic adverse reactions."
)

dry_skin = SkinType.objects.get(name='Dry Skin')
for routine in [cleansing_dry, exfoliation_dry, hydration_dry, sun_protection, drying_factors, aqua_consume]:
    routine.skin_types.add(dry_skin)

sensitive_skin= SkinType.objects.get(name='Sensitive Skin')
for routine in [cleansing_dry, no_exfoliation, hydration_dry, sun_protection, drying_factors, aqua_consume]:
    routine.skin_types.add(sensitive_skin)

normal_skin = SkinType.objects.get(name='Normal Skin')
for routine in [cleansing_normal, exfoliation_dry, hydration_normal, sun_protection, aqua_consume]:
    routine.skin_types.add(normal_skin)

combination_skin = SkinType.objects.get(name='Combination Skin')
for routine in [cleansing_dry, exfoliation_dry, hydration_comb, sun_protection, stop_acne, specialist_consultation, aqua_consume]:
    routine.skin_types.add(combination_skin)

oily_skin = SkinType.objects.get(name='Oily Skin')
for routine in [cleansing_oily, exfoliation_dry, hydration_comb, sun_protection, stop_acne, specialist_consultation, aqua_consume]:
    routine.skin_types.add(oily_skin)





dry_skin = AboutSkinTypes.objects.create(
    name="Dry Skin",
    description="Dry skin lacks moisture and may appear flaky or rough. It can feel tight and uncomfortable.",
    advantages="Less prone to acne, fewer breakouts.",
    disadvantages="Prone to fine lines and wrinkles, may feel tight or itchy."
)

normal_skin = AboutSkinTypes.objects.create(
    name="Normal Skin",
    description="Normal skin is well-balanced, neither too oily nor too dry. It has a smooth texture and few imperfections.",
    advantages="Well-balanced, healthy appearance.",
    disadvantages="May still experience occasional breakouts or dryness."
)

sensitive_skin = AboutSkinTypes.objects.create(
    name="Sensitive Skin",
    description="Sensitive skin is prone to irritation and redness. It may react to products or environmental factors easily.",
    advantages="Often fine-textured, may have fewer wrinkles.",
    disadvantages="Prone to redness, itching, and reactions to skincare products."
)

oily_skin = AboutSkinTypes.objects.create(
    name="Oily Skin",
    description="Oily skin produces excess sebum, leading to a shiny appearance and enlarged pores. It is prone to acne and breakouts.",
    advantages="Less prone to wrinkles, tends to age more slowly.",
    disadvantages="Prone to acne, enlarged pores, and excessive shine."
)

combination_skin = AboutSkinTypes.objects.create(
    name="Combination Skin",
    description="Combination skin has a mix of oily and dry areas. Typically, the T-zone (forehead, nose, and chin) is oily, while the cheeks may be dry.",
    advantages="Balanced hydration in different areas of the face.",
    disadvantages="May require different skincare routines for oily and dry areas."
)

