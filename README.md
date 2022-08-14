# AnomalyStudy

Faults are the primary culprits of breaking the high availability of cloud systems, even leading to costly outages. As the scale and complexity of clouds increase, it becomes extraordinarily difficult to understand, detect and diagnose faults. During outages, engineers record the detailed information of the whole life cycle of faults (i.e., fault occurrence, fault detection, fault identification, and fault mitigation) in the form of post-mortems. In this paper, we conduct a quantitative and qualitative study on 354 public post-mortems collected in three popular large-scale clouds, 97.7\% of which spans from 2015 to 2021.
<!-- 
## Objectives
 - Cloud Computing System
   - [Google](https://status.cloud.google.com/summary)
   - [AWS](https://aws.amazon.com/cn/premiumsupport/technology/pes/)
   - [Azure](https://status.azure.com/en-us/status/history/)
   -->
## Incidents Collection
  - [Azure](https://status.azure.com/en-us/status/history/)
  - [Google](https://status.cloud.google.com/summary)
  - [Facebook](https://developers.facebook.com/status/issues/)
  - [AWS](https://aws.amazon.com/cn/premiumsupport/technology/pes/)
  - [Kubernetes](https://github.com/hjacobs/kubernetes-failure-stories)
  - [Wikitech](https://wikitech.wikimedia.org/wiki/Category:Incident_documentation)
  - [Gitlab](https://gitlab.com/search?utf8=✓&search=outage&group_id=1112072&project_id=1304532&scope=issues&search_code=false&snippets=false&repository_ref=&nav_source=navbar)
  
## Prior datasets
 - https://github.com/danluu/post-mortems
 - https://ucare.cs.uchicago.edu/projects/cbs/ (Chicago datasets)
 - https://dsl.uwaterloo.ca/projects/neat/ (Unaccessible, latest version is required)
 - https://docs.google.com/spreadsheets/d/1YLuOTuve_naKwdZBnomzmiQW2XOn0rn-S7VvQ6YCtvc/edit#gid=1

## Our works
 - [post-mortem structured template](./anomaly_template.md)
 - [raw-public](./raw-public/)
 - [post-mortem structured collections](./anomaly_collection)


## Related Works
 - Gunawi H S, Hao M, Leesatapornwongsa T, et al. What bugs live in the cloud? a study of 3000+ issues in cloud systems[C]//Proceedings of the ACM Symposium on Cloud Computing. 2014: 1-14. [ref](https://ucare.cs.uchicago.edu/pdf/socc14-cbs.pdf)
 - Xu L, Dou W, Zhu F, et al. Experience report: A characteristic study on out of memory errors in distributed data-parallel applications[C]//2015 IEEE 26th International Symposium on Software Reliability Engineering (ISSRE). IEEE, 2015: 518-529. [ref](https://www.researchgate.net/profile/Jie_Liu190/publication/304291923_Experience_report_A_characteristic_study_on_out_of_memory_errors_in_distributed_data-parallel_applications/links/576e373108ae10de63962f64/Experience-report-A-characteristic-study-on-out-of-memory-errors-in-distributed-data-parallel-applications.pdf)
 - Alquraan A, Takruri H, Alfatafta M, et al. An analysis of network-partitioning failures in cloud systems[C]//13th {USENIX} Symposium on Operating Systems Design and Implementation ({OSDI} 18). 2018: 51-68.
MLA	[ref](https://www.usenix.org/system/files/osdi18-alquraan.pdf)
 - Gunawi H S, Hao M, Suminto R O, et al. Why does the cloud stop computing? Lessons from hundreds of service outages[C]//Proceedings of the Seventh ACM Symposium on Cloud Computing. 2016: 1-16. [ref](https://drj.com/wp-content/uploads/2018/07/socc16-cos.pdf)
 - Li Z, Liang M, O'brien L, et al. The cloud's cloudy moment: A systematic survey of public cloud service outage[J]. arXiv preprint arXiv:1312.6485, 2013. [ref](https://arxiv.org/pdf/1312.6485.pdf)
 - Aceto G, Botta A, Marchetta P, et al. A comprehensive survey on internet outages[J]. Journal of Network and Computer Applications, 2018, 113: 36-63. [ref](http://wpage.unina.it/giuseppe.aceto/pub/aceto2018comprehensive.pdf)
 - Sillito J, Kutomi E. Failures and Fixes: A Study of Software System Incident Response[J]. arXiv preprint arXiv:2008.11192, 2020. [ref](https://arxiv.org/abs/2008.11192)
 - Dingsøyr T. Postmortem reviews: purpose and approaches in software engineering[J]. Information and Software Technology, 2005, 47(5): 293-303. [ref](https://www.sciencedirect.com/science/article/pii/S0950584904001296)
 - Washburn Jr M, Sathiyanarayanan P, Nagappan M, et al. What went right and what went wrong: an analysis of 155 postmortems from game development[C]//Proceedings of the 38th International Conference on Software Engineering Companion. 2016: 280-289. [ref](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/washburn-icse-2016-2.pdf)

##