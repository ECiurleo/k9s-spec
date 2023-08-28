# k9s-spec

## To build a new version of k9s using Copr

1. Update k9s.spec to reflect the verison required

2. Build as SCM
https://copr.fedorainfracloud.org/coprs/emanuelec/k9s/add_build_scm/

3. The git URL is thi repo 
https://github.com/ECiurleo/k9s-spec.git

4. Select ¨Enable internet access during this build¨
![Screenshot of Copr Build screen with correct settings](images/screenshot.png)

The rest should remain default


Spec forked from 
https://git.myhypervisor.ca/dave/spec-files/-/tree/master/k9s