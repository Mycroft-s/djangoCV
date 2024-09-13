from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
def resume_view(request):
    context = {
        'name': 'Meng Hongdao',
        'phone': '+1-718-306-3737',
        'email': 'hm3424@nyu.edu / mycrofthd@gmail.com',
        'address': '#111 Lawrence St, Brooklyn, New York, 11201',
        'education': [
            {
                'institution': 'NYU Tandon School of Engineering',
                'degree': 'Master of Engineering',
                'duration': '09/2024—present',
                'major': 'Computer Science',
                'core_modules': ['Web Search Engines', 'Software Engineering', 'Artificial Intelligence']
            },
            {
                'institution': 'Beijing University of Technology (BJUT)',
                'degree': 'Bachelor of Engineering',
                'duration': '09/2020—07/2024',
                'major': 'Information Security',
                'gpa': '3.60/4.00',
                'core_modules': ['Network Protocol Analysis', 'Object-Oriented Programming', 'Information Theory and Coding','Computer Networks','Principles of Computer Organization']
            }
        ],
        'experience': [
            {
                'role': 'AI Algorithm Engineer (Intern)',
                'company': 'TAL Education Group',
                'duration': '03/2024—07/2024',
                'description': [
                    'Researched LLM, Transformer, Retrival Augmented Generation (RAG)',
                    'Optimized bgem3 hybrid search and instantiated embedding and re-rank methods'
                ]
            },
            {
                'role': 'Researcher & 1st Author',
                'lab': 'Data Mining & Security (DMS) Lab, BJUT',
                'duration': '09/2022—07/2024',
                'description': [
                    'Researched federated learning, multi-view multi-label machine learning',
                    'Proposed a new method of FMVML and wrote papers to apply for patents'
                ]
            }
        ],
        'skills': ['Python', 'Django', 'JavaScript', 'HTML', 'C++', 'Machine Learning'],
        'hobbies': ['Photography', 'Public Speaking', 'Swimming', 'Badminton', 'Football']
    }
    return render(request, 'cv/resume.html', context)



def projects_view(request):
    context = {
        'projects': [
            {
                'role': 'AI Algorithm Engineer (Intern)',
                'company': 'TAL Education Group',
                'duration': '03/2024—07/2024',
                'description': [
                    'Researched LLM, Transformer, Retrieval Augmented Generation (RAG)',
                    'Optimized bgem3 hybrid search and instantiated embedding and re-rank methods',
                    'Learned the communication and cooperation in real work and the workflow on GitLab'
                ]
            },
            {
                'role': 'Researcher & 1st Author',
                'lab': 'Data Mining & Security (DMS) Lab, BJUT',
                'duration': '09/2022—07/2024',
                'description': [
                    'Researched federated learning, multi-view multi-label machine learning',
                    'Proposed a new method of FMVML and wrote papers to apply for patents',
                    'Gained skills in literature review, academic writing, and mathematical optimization methods'
                ]
            },
            {
                'role': 'Web Designer',
                'project': 'Realization of Algorithm for Traveling Salesmen Based on Baidu Map API',
                'duration': '09/2022—12/2022',
                'description': [
                    'Used front-end technologies (CSS, HTML, JavaScript)',
                    'Developed navigation system using Baidu Map API for traveling salesman algorithm'
                ]
            },
            {
                'role': 'Researcher',
                'lab': 'Beijing Key Laboratory of Clinical Epidemiology, Capital Medical University',
                'duration': '09/2021—present',
                'description': [
                    'Participated in group meetings, read literature on multi-omics data integration methods based on machine learning',
                    'Worked on writing academic literature reviews and papers',
                    'Mastered the statistical methods of constructing prediction models using R'
                ]
            },
            {
                'role': 'Researcher & 1st Author',
                'lab': 'Research on Organizational Capacity of Public Hospitals and Impact Mechanism of TheirMaturity on Hospital Efficiency(Project No. 9222004) Beijing National Science Foundation Researcher ',
                'duration': '09/2021—09/2022',
                'description': [
                    'Learned the bibliometric method and applied the bibliometric software packages Citespace and NoteExpress',
                    'Wrote the paper titled Visualized Quantitative Analysis of Hot Research Topics about Medical Information Security in China in the Internet Age independently'
                ]
            },
            {
                'role': 'Researcher',
                'lab': 'Research on Remote Monitoring System for Families with Elders Based on the Internet of Things and  Cloud  Computing  Platform  (Project  No.  71661167001),  National  Natural  Science  Foundation  International (Regional) Cooperation Program      ',
                'duration': '04/2021—09/2021 ',
                'description': [
                    'Took part in webpage development in the research AI Smart Clothes—Pioneer of Remote Monitoring for Arrhythmic Elders',
                    'Self studied JavaScript and developed the interaction part for the back-end web platform'
                ]
            },
            {
                'role': 'Project Leader',
                'project': 'Complicated Page Analysis Based on Machine Learning, BJUT Spark Program',
                'duration': '09/2020—12/2021',
                'description': [
                    'Led a team studying page analysis using machine learning techniques',
                    'Wrote research reports and managed project timelines'
                ]
            },
            {
                'role': 'Leader and  Researcher',
                'project': 'A  Cohort  Study  of Natural  Population with  Chronic Diseases  in  Living  Communities  of the Beijing-Tianjin-Hebei Region (Project No. 2016YFC0900603), National Key Research and Development Plan',
                'duration': '07/2020—12/2020',
                'description': [
                    'Assisted the project leader in recruiting more than 50 volunteers',
                    'Took part in questionnaire survey, data input and biological specimen repository construction'
                ]
            }
        ]
    }
    return render(request, 'cv/projects.html', context)

    return render(request, 'cv/projects.html', context)

def contact_view(request):
    # 联系页面视图
    return render(request, 'cv/contact.html')


from django.shortcuts import render

def awards_view(request):
    context = {
        'awards': [
            {
                'title': 'Second Prize (university level), 5th “BJUT Cup” Innovation and Entrepreneurship Competition',
                'description': 'Preliminary of 8th China International College Students “Internet Plus” Innovation and Entrepreneurship Competition for the research AI Smart Clothes—Pioneer of Remote Monitoring for Arrhythmic Elders (07/2022)'
            },
            {
                'title': 'Second Prize (Beijing municipal level), 5th BJUT iCAN Competition',
                'description': 'Awarded for the research AI Smart Clothes—Pioneer of Remote Monitoring for Arrhythmic Elders (07/2022)'
            }
        ],
        'publications': [
            {
                'title': 'Federated Multi-view Multi-Label Classification',
                'authors': 'Hongdao Meng, Gengyu Lyu, Songhe Feng, Yipeng Wang, and Zhen Yang',
                'journal': 'IEEE Transactions on Big Data (2023) (major revision)'
            },
            {
                'title': 'Susceptibility genes identification and risk evaluation model construction by transcriptome-wide association analysis for salt sensitivity of blood pressure: the EpiSS study',
                'authors': 'Han Qi, Yunyi Xie, Xiaojun Yang, Juan Xia, Kuo Liu, Fengxu Zhang, Wenjuan Peng, Fuyuan Wen, Bingxiao Li, Bowen Zhang, Xinyue Yao, Boya Li, Hongdao Meng, Zumin Shi, Wang Yang, Ling Zhang',
                'journal': 'BMC Genomics (2024) (accept)',
                'url': 'https://doi.org/10.1186/s12864-024-10409-9'
            },
            {
                'title': 'Visualized Quantitative Analysis of Hot Research Topics about Medical Information Security in China in the Internet Age',
                'authors': 'Hongdao Meng, Kai Meng',
                'journal': 'Chinese Hospital Management (2023) (under review)'
            },
            {
                'title': 'Progress in the application of multi-omics big data analysis in the study of hypertension',
                'authors': 'Han Qi, Xiaojun Yang, Fuyuan Wen, Hongdao Meng, Ling Zhang',
                'journal': 'Chinese Journal of Cardiology (2023) (to be published)'
            },
            {
                'title': 'Key methods of multi-modal information fusion based on data privacy protection',
                'authors': 'Gengyu Lyu, Hongdao Meng',
                'journal': 'National Intellectual Property Administration. Patent for invention. Application number: 2023111952962 (2023) (to be accepted)'
            },
            {
                'title': 'Research on Status Quo and Effectiveness Evaluation of the Family-School Interaction Models Adopted by a Middle School in Beijing',
                'authors': 'Hongdao Meng, Fang Yu, Hongying Liu, Caixiang Yan, Ling Zhang',
                'journal': 'Education for Chinese After-school (Theory), 2017, 594(12):1-2+10.DOI:10.3969/j.issn.1004-8502. 2017. 04. 001'
            }
        ]
    }
    return render(request, 'cv/awards.html', context)

