Name:           bpftrace
Version:        0.10.0
Release:        1
Summary:        High-level tracing language for Linux eBPF
License:        ASL 2.0

URL:            https://github.com/iovisor/bpftrace
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Arches will be included as upstream support is added and dependencies are
# satisfied in the respective arches
ExclusiveArch:  x86_64 %{power64} aarch64

BuildRequires:  gcc-c++ bison flex cmake elfutils-libelf-devel
BuildRequires:  zlib-devel llvm-devel clang-devel
BuildRequires:  bcc-devel >= 0.11.0-2
BuildRequires:  libbpf-devel libbpf-static
BuildRequires:  binutils-devel


%description
bpftrace is a high-level tracing language for Linux enhanced Berkeley Packet
Filter (eBPF) available in recent Linux kernels (4.x). bpftrace uses LLVM as a
backend to compile scripts to BPF-bytecode and makes use of BCC for
interacting with the Linux BPF system, as well as existing Linux tracing
capabilities: kernel dynamic tracing (kprobes), user-level dynamic tracing
(uprobes), and tracepoints. The BPFtrace language is inspired by awk and C,
and predecessor tracers such as DTrace and SystemTap.


%prep
%autosetup -p1


%build
%cmake . \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DBUILD_TESTING:BOOL=OFF \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DLIBBCC_LIBRARIES:PATH=/usr/lib64/libbcc-no-libbpf.so
%make_build


%install
%make_install

find %{buildroot}%{_datadir}/%{name}/tools -type f -exec \
  sed -i -e '1s=^#!/usr/bin/env %{name}\([0-9.]\+\)\?$=#!%{_bindir}/%{name}=' {} \;


%files
%doc README.md CONTRIBUTING-TOOLS.md
%doc docs/reference_guide.md docs/tutorial_one_liners.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tools
%dir %{_datadir}/%{name}/tools/doc
%{_bindir}/%{name}
%{_mandir}/man8/*
%attr(0755,-,-) %{_datadir}/%{name}/tools/*.bt
%{_datadir}/%{name}/tools/doc/*.txt


%changelog
* Thu May 07 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.10.0-1
- Package init
