clear all;
close all;
clc;

load 'data/gsm_4c_in.mat'
load 'data/gsm_4c_out.mat'


% AM - AM
figure()
plot(abs(x), abs(y), '.')

% AM - PM
figure()
plot(abs(x), angle(x.*conj(y)), '.')

