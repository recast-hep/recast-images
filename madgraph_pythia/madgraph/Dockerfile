FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install python2.7 gcc gfortran g++ make python-pip wget gnuplot bc cmake rsync
RUN pip install numpy scipy
RUN mkdir /code
WORKDIR /code
ARG MADGRAPH_VERSION="2.6.6"
RUN echo "Madgraph version is ${MADGRAPH_VERSION}"
RUN ["/bin/bash", "-c", "wget https://launchpad.net/mg5amcnlo/${MADGRAPH_VERSION:0:1}.0/${MADGRAPH_VERSION:0:3}.x/+download/MG5_aMC_v${MADGRAPH_VERSION}.tar.gz"]
RUN ["/bin/bash", "-c", "tar -xzf MG5_aMC_v${MADGRAPH_VERSION}.tar.gz; rm MG5_aMC_v${MADGRAPH_VERSION}.tar.gz; mv MG5_aMC_v${MADGRAPH_VERSION:0:1}_${MADGRAPH_VERSION:2:1}_${MADGRAPH_VERSION:4:1} madgraph"]
RUN cd madgraph; echo "install ninja" >> install.dat; echo "install collier" >> install.dat; echo "install oneloop" >> install.dat; echo "install looptools" >> install.dat; echo "install QCDLoop" >> install.dat; ./bin/mg5_aMC install.dat; rm install.dat
RUN cd madgraph/vendor/CutTools; make clean; make
RUN cd madgraph/vendor/IREGI/src; make clean; make
RUN echo "export PYTHONPATH=/code/madgraph/HEPTools/lhapdf6/lib/python2.7/site-packages" >> ~/.profile; echo "export LD_LIBRARY_PATH=/code/madgraph/HEPTools/lhapdf6/lib" >> ~/.profile;
ADD steer_madgraph.py .