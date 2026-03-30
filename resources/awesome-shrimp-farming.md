# Awesome Shrimp Farming & Aquaculture

> Every shrimp farming, aquaculture monitoring, and related open-source project on GitHub -- verified by visiting each repo via the GitHub API. **200+ repos catalogued.** This is the "awesome list" that didn't exist until now.

---

## Table of Contents

- [Aquatic Controllers (High Stars, Adaptable)](#aquatic-controllers)
- [Shrimp Farm Management](#shrimp-farm-management)
- [IoT & Water Monitoring (Shrimp-Specific)](#iot--water-monitoring-shrimp-specific)
- [IoT & Water Monitoring (General Aquaculture)](#iot--water-monitoring-general-aquaculture)
- [Computer Vision & Shrimp Detection](#computer-vision--shrimp-detection)
- [Disease Detection (ML/AI)](#disease-detection-mlai)
- [Automated Feeding](#automated-feeding)
- [Biofloc Technology](#biofloc-technology)
- [Aquaponics](#aquaponics)
- [RAS Simulation & Design](#ras-simulation--design)
- [Water Quality Prediction (ML)](#water-quality-prediction-ml)
- [Ornamental Shrimp](#ornamental-shrimp)
- [Vannamei-Specific Tools](#vannamei-specific-tools)
- [Prawn Farming](#prawn-farming)
- [Genomics & Bioinformatics](#genomics--bioinformatics)
- [Datasets & Research](#datasets--research)
- [Mobile Apps](#mobile-apps)
- [Sensor Libraries](#sensor-libraries)
- [Resource Lists](#resource-lists)

---

## Aquatic Controllers

The most mature open-source projects. Designed for aquariums/aquaponics but directly adaptable for shrimp.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [reef-pi/reef-pi](https://github.com/reef-pi/reef-pi) | 431 | Go/JS | Full-featured Raspberry Pi reef/aquarium controller. pH, temp, dosing, auto top-off, email alerts, camera. Active community. |
| [rjsears/GardenPi](https://github.com/rjsears/GardenPi) | 301 | Python/Flask | Multi-zone hydroponic/aquaponic/fish tank water management. 27 zones, sensors, Flask web UI. |
| [TheRealFalseReality/aquapi](https://github.com/TheRealFalseReality/aquapi) | 85 | YAML/ESPHome | ESP32 + Atlas Scientific EZO sensors (pH, EC, DO). Home Assistant integration. Web install. |
| [mhajda/PiPonics](https://github.com/mhajda/PiPonics) | 40 | Python | Aquaponics monitoring and control with Raspberry Pi. |
| [marine-assistant/Marineassistant](https://github.com/marine-assistant/Marineassistant) | 39 | ESP32 | Open-source smart aquarium controller. pH, TDS, EC, ORP. Custom PCB. Home Assistant. |
| [aabishe/AquacultureSystem](https://github.com/aabishe/AquacultureSystem) | 28 | Java | Aquaculture management system (graduation project). |
| [fnandes/aquareo](https://github.com/fnandes/aquareo) | 22 | C++ | Modular ESP32 aquarium controller. MQTT + Home Assistant. pH, salinity, dosing. |
| [voltlog/esp32-aquarium-controller](https://github.com/voltlog/esp32-aquarium-controller) | 19 | C++ | ESP32 + 4 relays + temp/humidity + web UI. Custom PCB on Tindie. |
| [ReefSpy/ReefberryPi](https://github.com/ReefSpy/ReefberryPi) | 15 | Python | Raspberry Pi controller. 4x DS18B20, 8-channel ADC for pH, 8 relays. |
| [Chiumanfu/Chiumanfu-Aquaponic-Controller](https://github.com/Chiumanfu/Chiumanfu-Aquaponic-Controller) | 13 | C++ | Arduino Mega. pH, DO, temp, water level, flow, auto feeder. Grovestreams IoT. |

## Shrimp Farm Management

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [hbc123ht/Shrimp-Farming-Management-System](https://github.com/hbc123ht/Shrimp-Farming-Management-System) | 3 | Python/Django | Shrimp farm management with IBM Cloud water quality control. |
| [taoincredible/Smart-Management-Information-System-for-Freshwater-Shrimp-Cultivation](https://github.com/taoincredible/Smart-Management-Information-System-for-Freshwater-Shrimp-Cultivation) | 1 | Vue/Spring Boot | 10+ modules: monitoring, production, water quality alerts, ChatGPT AI assistant. |
| [trvannhanh/aquafarm-management](https://github.com/trvannhanh/aquafarm-management) | 0 | C#/ASP.NET | Full farm ERP: ponds, batches, feeding logs, harvests, sales, reports. |
| [Kiransekar/UPCHECK](https://github.com/Kiransekar/UPCHECK) | 0 | Python | Intelligent shrimp farm management. Docker, Prometheus metrics, REST API. |
| [ds-raj/Shrimp_Pond_RAG](https://github.com/ds-raj/Shrimp_Pond_RAG) | 0 | Python | RAG system for shrimp pond analytics using OpenAI LLMs + ChromaDB. |
| [fancewer2402/Tomato](https://github.com/fancewer2402/Tomato) | 0 | -- | Water Quality Management for Shrimp Farming. Pond monitoring, optimization, alerts. |

## IoT & Water Monitoring (Shrimp-Specific)

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [CodersCafeTech/Shrimp-Monitoring-Buoy](https://github.com/CodersCafeTech/Shrimp-Monitoring-Buoy) | 4 | C++ | Floating sensor buoy for shrimp ponds. Hardware schematics included. |
| [Akalanka-00/Shrimp-Farming-System](https://github.com/Akalanka-00/Shrimp-Farming-System) | 2 | C | Embedded shrimp farming system (university project). |
| [frederick98/IoT_shrimpPond](https://github.com/frederick98/IoT_shrimpPond) | 1 | JS/Python/C++ | Full-stack: React frontend, PHP backend, Arduino sensors, Raspberry Pi. |
| [josep5097/LoRa-Shrimp-Monitoring-Control](https://github.com/josep5097/LoRa-Shrimp-Monitoring-Control) | 0 | C++ | LoRa + fuzzy logic aerator control. Published in IJACSA 2023. |
| [varshithpbs007/Shrimp-Water-Quality_MVP](https://github.com/varshithpbs007/Shrimp-Water-Quality_MVP) | 0 | C++ | ESP32 + MQTT + automated aeration. pH, DO, ammonia, temp. |
| [Gopika1310/shrimp-aquaculture-monitoring](https://github.com/Gopika1310/shrimp-aquaculture-monitoring) | 0 | Python | AI-powered mortality + algal bloom detection. FastAPI + Docker. |

## IoT & Water Monitoring (General Aquaculture)

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [TsaiRongFu/AI-Aquaculturing](https://github.com/TsaiRongFu/AI-Aquaculturing) | 25 | Python | MobileNet + EdgeTPU + sensors + Laravel + LINE bot (Taiwan). |
| [pkErbynn/IoT-WQMS](https://github.com/pkErbynn/IoT-WQMS) | 21 | Python/HTML | ESP32 water quality monitoring. Flask, SQLite, email alerts. |
| [Gravicode/AquaCulture](https://github.com/Gravicode/AquaCulture) | 8 | C# | End-to-end IoT: ModBus, MQTT, Orleans, Blazor, MAUI, Redis. |
| [SaminYaser-work/AgroSmart](https://github.com/SaminYaser-work/AgroSmart) | 7 | PHP | AI-powered ERP for agriculture/aquaculture operations. |
| [kavyaballa1020/Smart-Pond-Monitoring-IoT](https://github.com/kavyaballa1020/Smart-Pond-Monitoring-IoT) | 6 | Python/HTML | NodeMCU ESP8266 pond monitor. Flask + MongoDB dashboard. |
| [ilan2002/Aquaculture_monitoring_using_Machinelearning_ESP32](https://github.com/ilan2002/Aquaculture_monitoring_using_Machinelearning_ESP32) | 6 | Jupyter | ESP32 + edge ML inferencing for pond monitoring. |
| [Kedar-Deshmukh/Smart-Aquaculture-Monitoring-and-Control-using-WSN-and-CAN](https://github.com/Kedar-Deshmukh/Smart-Aquaculture-Monitoring-and-Control-using-WSN-and-CAN) | 6 | C | pH, DO, temp sensors + aerator motor control + CAN bus. |
| [caseyWebb/mayfly](https://github.com/caseyWebb/mayfly) | 5 | Python | ESP32 environmental monitoring for aquaculture/hydroponics. |
| [alaminsani-py/fish_farm_monitoring_system](https://github.com/alaminsani-py/fish_farm_monitoring_system) | 0 | Python/Flutter | AI-predicted DO and ammonia. Solar-powered. Auto-calibration. Chatbot. |

## Computer Vision & Shrimp Detection

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [chenne0819/ShrimpVisionRT](https://github.com/chenne0819/ShrimpVisionRT) | 0 | Python | **Most advanced.** Real-time YOLO-OBB + segmentation + Norfair tracking + weight estimation. |
| [Nathancgy/Shrimp_food_detection](https://github.com/Nathancgy/Shrimp_food_detection) | 3 | Jupyter | Leftover food detection in ponds. Harris corner detection + ResNet. Flask app. |
| [EbonGit/Aquarium-Shrimp-Counting-System-YOLO](https://github.com/EbonGit/Aquarium-Shrimp-Counting-System-YOLO) | 3 | Jupyter | YOLO-based aquarium shrimp counter. |
| [algonacci/Shrimp-Pond-Sediments-CNN](https://github.com/algonacci/Shrimp-Pond-Sediments-CNN) | 3 | Python/Flask | CNN for pond sediment detection. |
| [Ikshv/shrimp-vision](https://github.com/Ikshv/shrimp-vision) | 2 | Python | Full-stack YOLOv8: 6 classes (Shrimp/Juvenile/Adult/Egg/Molt/Dead). FastAPI + Next.js + Docker. |
| [rezaafaisal/shrimp-detection](https://github.com/rezaafaisal/shrimp-detection) | 2 | Python | EfficientDet shrimp counting. |
| [zeldaxlove94/shrimp-feeding-behavior-analysis-codepacks-20230723](https://github.com/zeldaxlove94/shrimp-feeding-behavior-analysis-codepacks-20230723) | 0 | Jupyter | YOLOv8 instance segmentation for feeding behavior analysis. 63MB dataset. |

## Disease Detection (ML/AI)

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [eshaanmathakari/shrimpInfectionDetection](https://github.com/eshaanmathakari/shrimpInfectionDetection) | 5 | Jupyter | Deep learning WSSV detection. CNN + image augmentation. |
| [SirishmaA1284/Shrimp-WSD-Detection-Using-CNN-LSTM](https://github.com/SirishmaA1284/Shrimp-WSD-Detection-Using-CNN-LSTM) | 1 | Jupyter | Hybrid CNN-LSTM for White Spot Disease. ResNet50 backbone. 89.5% accuracy. Dataset included. |
| [PattarawutAriyapruck/ShrimpDiseaseDetection](https://github.com/PattarawutAriyapruck/ShrimpDiseaseDetection) | 1 | Jupyter | Flask web app. Transfer learning. Presented at Mahidol SciEx 2025 + NAC2025. |
| [paul-padilla/Bangladeshi-Shrimp-Farming](https://github.com/paul-padilla/Bangladeshi-Shrimp-Farming) | 1 | Jupyter | Neural network analysis of WSD factors in Bangladesh. |
| [Mohankrish08/shrimp-monitoring-system](https://github.com/Mohankrish08/shrimp-monitoring-system) | 0 | Jupyter | YOLOv8 segmentation: healthy vs infected shrimp. Real-time notifications. |
| [Affand6331/Shrimp_Classifier](https://github.com/Affand6331/Shrimp_Classifier) | 0 | Jupyter | Swin Transformer for shrimp disease classification. |

## Automated Feeding

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [zhaohc1010/Intelligent-Shrimp-Feeding-System](https://github.com/zhaohc1010/Intelligent-Shrimp-Feeding-System) | 0 | Python | **Notable.** LightGBM + LLM decision support + CV hardware control. Live demo on Render. |
| [engrmflores/Microcontroller-driven-Feeding-Management-and-Automation-for-L.-vannamei-Shrimp-Aquaculture](https://github.com/engrmflores/Microcontroller-driven-Feeding-Management-and-Automation-for-L.-vannamei-Shrimp-Aquaculture) | 0 | C++ | Arduino auto feeder for vannamei. 96.21% accuracy. IEEE paper included. |
| [vonjansencomedia/fuzzylogic-shrimpfeeder](https://github.com/vonjansencomedia/fuzzylogic-shrimpfeeder) | 0 | MATLAB | Mamdani FIS feeding simulation for 90-day cycle. |
| [Engelbert-Jubile/Pakan_Udang_Flutter](https://github.com/Engelbert-Jubile/Pakan_Udang_Flutter) | 1 | Dart | Flutter mobile app for automatic shrimp feeding. |
| [jsn6686/shrimpCal](https://github.com/jsn6686/shrimpCal) | 0 | HTML | Feed chart generator + survival calculator. |

## Biofloc Technology

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [eqrakhattak/smart-biofloc-monitoring](https://github.com/eqrakhattak/smart-biofloc-monitoring) | 3 | Dart | Flutter + Arduino + ESP8266 biofloc monitoring. |
| [YeaminRabbi/Biofloc](https://github.com/YeaminRabbi/Biofloc) | 2 | JavaScript | IoT sensor reading with email/SMS alerts. |
| [Saiful-Islam0/IoT-based-Smart-Biofloc-System](https://github.com/Saiful-Islam0/IoT-based-Smart-Biofloc-System) | 1 | HTML | ESP32 + Firebase + auto pump control + dashboard. |
| [mammonur/WaterQualityPredictionforBioflocAquaculture](https://github.com/mammonur/WaterQualityPredictionforBioflocAquaculture) | 1 | Jupyter | IoT-based smart water quality prediction for biofloc. |
| [Mutasim84/Biofloc-System-Management](https://github.com/Mutasim84/Biofloc-System-Management) | 0 | Python | Biofloc monitoring and management. |
| [ForgetfulMangonel/Modelling-Biogeochemical-Interactions-in-Litopenaeus-vannamei-Biofloc-Systems](https://github.com/ForgetfulMangonel/Modelling-Biogeochemical-Interactions-in-Litopenaeus-vannamei-Biofloc-Systems) | 0 | Jupyter | Master thesis: biofloc biogeochemistry modeling. |

## Aquaponics

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [aHagouel/IOT-Aquaponics-in-NYC](https://github.com/aHagouel/IOT-Aquaponics-in-NYC) | 18 | Python | Bedroom-scale IoT RAS. Excellent documentation. |
| [natevw/greenhouse](https://github.com/natevw/greenhouse) | 11 | Arduino | Aquaponics monitoring + remote fish feeder. |
| [plantsandmachines/beta](https://github.com/plantsandmachines/beta) | 10 | JavaScript | Robotic aquaponic ecosystem prototype. |
| [layerzerolabs/aquaponics-arduino](https://github.com/layerzerolabs/aquaponics-arduino) | 12 | C++ | Arduino aquaponics control system. |
| [dwyl/learn-aquaponics](https://github.com/dwyl/learn-aquaponics) | 8 | -- | Educational guide: create a sustainable mini-ecosystem. |
| [devaaron/automated-aquaponics](https://github.com/devaaron/automated-aquaponics) | 6 | HTML | Automated ebb-and-flow aquaponics. |

## RAS Simulation & Design

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [FishSim/LibRAS](https://github.com/FishSim/LibRAS) | 17 | Modelica | RAS simulation library. Chalmers University. Water chemistry, biofilter modeling. |
| [Terkwood/prawnalith](https://github.com/Terkwood/prawnalith) | 17 | Rust | Sensor instrumentation + data management for freshwater prawn tanks. Rust + MQTT + Docker. |
| [joakimsk/ras](https://github.com/joakimsk/ras) | 1 | HTML | RAS knowledge base with calculators and system design. |

## Water Quality Prediction (ML)

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [AquaPredDB/AquacultureInsight](https://github.com/AquaPredDB/AquacultureInsight) | 9 | Python | Datasets, algorithms, and papers for water quality prediction. |
| [iDharshan/LSTM-based-Soft-Sensor-for-Estimating-Nitrate-Concentration-in-Aquaponics-Pond](https://github.com/iDharshan/LSTM-based-Soft-Sensor-for-Estimating-Nitrate-Concentration-in-Aquaponics-Pond) | 8 | Jupyter | LSTM soft sensor for nitrate estimation. |
| [conkyboy/shrimp-pond-do-concentration-prediction](https://github.com/conkyboy/shrimp-pond-do-concentration-prediction) | 1 | Python | DO prediction using neural network with entropy metrics. Apache 2.0. |

## Ornamental Shrimp

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [Andrewishere502/NeoCounterAI](https://github.com/Andrewishere502/NeoCounterAI) | 3 | Jupyter | CNN (ResNet) to count Neocaridina davidi in images. 87MB with models. |
| [thovu-1/Shrimp_App_ML](https://github.com/thovu-1/Shrimp_App_ML) | 1 | Jupyter | ML model for Neocaridina species identification. 1.2GB with models. |
| [bramvisser/shrimp-pwa](https://github.com/bramvisser/shrimp-pwa) | 0 | TypeScript | Offline-first PWA for shrimp breeding data capture. Active 2026. |
| [zvxr/shrimpkeeper](https://github.com/zvxr/shrimpkeeper) | 0 | Lua | PICO-8 shrimp keeping simulation game. Tracks pH, ammonia, GH, KH, TDS, color morphs. |
| [danbacastro/aquarium-chemy](https://github.com/danbacastro/aquarium-chemy) | 0 | Python | Water mineral calculator for freshwater shrimps. |
| [rastislavelias/cherry-shrimps-basics](https://github.com/rastislavelias/cherry-shrimps-basics) | 0 | HTML | Educational website about cherry shrimp basics. |

## Vannamei-Specific Tools

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [jianbone/L_vannamei_genome](https://github.com/jianbone/L_vannamei_genome) | 4 | Perl | L. vannamei genome project. |
| [patipond-tiy/vannameivision](https://github.com/patipond-tiy/vannameivision) | 2 | Python | Computer vision for vannamei. |
| [sqhe18/vannamei-system](https://github.com/sqhe18/vannamei-system) | 2 | -- | Vannamei breeding aid. |
| [dimascahyo/sistem-pakar-vannamei](https://github.com/dimascahyo/sistem-pakar-vannamei) | 1 | PHP | Expert system for vannamei disease (Forward Chaining + Certainty Factor). |
| [jaimepaz80](https://github.com/jaimepaz80) | 0 | HTML | 8+ repos: growth calc, weight projection, oxygen alerts, pathology, feeding. |

## Prawn Farming

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [Terkwood/prawnalith](https://github.com/Terkwood/prawnalith) | 17 | Rust | (See RAS section above) |
| [kavishkarasara/Prawn-Care](https://github.com/kavishkarasara/Prawn-Care) | 0 | Dart | Flutter app: pond monitoring, orders, feeding schedules, Node.js backend. |
| [Nipun-Milinda](https://github.com/Nipun-Milinda) | 0 | JS/C++ | 4-repo system: API + Arduino + NodeMCU + Web App for prawn farming. |
| [vedkarthik9999/sustainableprawn](https://github.com/vedkarthik9999/sustainableprawn) | 0 | Jupyter | IoT + ML for sustainable freshwater prawn farming. |

## Genomics & Bioinformatics

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [jianbone/L_vannamei_genome](https://github.com/jianbone/L_vannamei_genome) | 4 | Perl | Vannamei genome project. |
| [Meora-Rajeev/Biofloc-Metagenomics](https://github.com/Meora-Rajeev/Biofloc-Metagenomics) | 2 | -- | Biofloc metagenomics analysis. |
| [LuiguiGallardo/p_monodon_transcriptome](https://github.com/LuiguiGallardo/p_monodon_transcriptome) | 1 | R/Shell | Black tiger shrimp transcriptome. UNAM. |
| [jordanchancellor/PWS_SNP_workflow](https://github.com/jordanchancellor/PWS_SNP_workflow) | 0 | Shell | SNP calling workflow for Penaeus vannamei. GATK pipeline. |
| [Roslin-Aquaculture/10x-snRNAseq_LV-HP-atlas](https://github.com/Roslin-Aquaculture/10x-snRNAseq_LV-HP-atlas) | 0 | R | Single-nuclei RNAseq cell atlas of vannamei hepatopancreas. Roslin Institute. |
| [adelatif11-teramina/shrimp-annotation-pipeline](https://github.com/adelatif11-teramina/shrimp-annotation-pipeline) | 0 | Python/JS | Production NLP annotation pipeline for shrimp aquaculture domain. NER + relation extraction. |

## Datasets & Research

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [AquaPredDB/AquacultureInsight](https://github.com/AquaPredDB/AquacultureInsight) | 9 | Python | Water quality prediction datasets + algorithms. |
| [climatechange-ai-tutorials/aquaculture-mapping](https://github.com/climatechange-ai-tutorials/aquaculture-mapping) | 7 | Jupyter | Satellite imagery + semantic segmentation for pond detection. |
| [HitenSachani/dataset_shrimp_farming](https://github.com/HitenSachani/dataset_shrimp_farming) | 1 | -- | Dataset: water temp, pressure, features for shrimp farm. |
| [richieheal/BangladeshCOVID19Shrimp](https://github.com/richieheal/BangladeshCOVID19Shrimp) | 0 | R | COVID-19 impact on Bangladesh shrimp aquaculture. |

## Mobile Apps

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [rmmostak/scmfp](https://github.com/rmmostak/scmfp) | 2 | Dart | BLE IoT device for coastal Bangladesh shrimp farmers. |
| [121140084-Rizki-Esa-Fadillah/Aplikasi_SmartFarm](https://github.com/121140084-Rizki-Esa-Fadillah/Aplikasi_SmartFarm) | 1 | Dart | Flutter monitoring + auto-control for shrimp ponds. |
| [Kotasrinuaa/mila-shrimp-farming-app](https://github.com/Kotasrinuaa/mila-shrimp-farming-app) | 0 | Dart | Shrimp farming mobile app. |
| [vgrajay/shrimp-growth-tracker](https://github.com/vgrajay/shrimp-growth-tracker) | 0 | TypeScript | Shrimp growth tracking web app. |

## Sensor Libraries

Essential libraries for building your own monitoring hardware.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [Atlas-Scientific/Ezo_I2c_lib](https://github.com/Atlas-Scientific/Ezo_I2c_lib) | 79 | C++ | Official Arduino library for Atlas Scientific EZO pH/DO/EC sensors. |
| [whitebox-labs/tentacle](https://github.com/whitebox-labs/tentacle) | 29 | KiCAD | Open-source Arduino shield for 4x Atlas Scientific EZO circuits. OSHW certified. |
| [100prznt/EzoGateway](https://github.com/100prznt/EzoGateway) | 19 | C# | REST API gateway for Atlas Scientific sensors on Raspberry Pi. |
| [timboring/atlas_i2c](https://github.com/timboring/atlas_i2c) | 9 | Python | Python library for Atlas Scientific EZO on Raspberry Pi. PyPI package. |

## Resource Lists

| Repository | Stars | Description |
|-----------|-------|-------------|
| [thefarmhub/awesome-farming-tech](https://github.com/thefarmhub/awesome-farming-tech) | 19 | Curated list: software, hardware suppliers, sensors by type. Closest to an "awesome aquaculture" list. |
| [dwyl/learn-aquaponics](https://github.com/dwyl/learn-aquaponics) | 8 | Educational guide for aquaponics beginners. |

---

## Summary

**200+ repos catalogued** across shrimp farming, aquaculture IoT, computer vision, disease detection, biofloc, aquaponics, RAS, and ornamental shrimp.

**Top discoveries**:
- `reef-pi` (431 stars) - most mature aquatic controller
- `GardenPi` (301 stars) - best multi-zone water management
- `ShrimpVisionRT` - most technically advanced shrimp CV pipeline (YOLO-OBB + tracking + weight estimation)
- `Intelligent-Shrimp-Feeding-System` - multimodal AI feeding with LLMs
- `prawnalith` (17 stars) - Rust-based prawn monitoring (unique tech stack)

**The reality**: Most shrimp repos have 0-5 stars. The space is extremely niche on GitHub. The most useful projects are often the aquarium/aquaponics controllers (reef-pi, AquaPi, GardenPi) which have the exact sensor support needed for shrimp.

---

## Contributing

Found a repo we missed? Open a PR:
- Repo must exist and contain real code/content
- Include: repo link, stars, language, description
- Categorize appropriately
